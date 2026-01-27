import inspect
import json
import logging
import os
from enum import Enum
from os import PathLike
from pathlib import Path
from subprocess import CalledProcessError, CompletedProcess, run
from typing import Any, Dict, List, Optional, Type, TypeVar

from pydantic import BaseModel, PydanticInvalidForJsonSchema
from pydantic.json_schema import (
    GenerateJsonSchema,
    JsonSchemaMode,
    JsonSchemaValue,
    _deduplicate_schemas,
)
from pydantic_core import PydanticOmit, core_schema, to_jsonable_python
from semver import Version

from ..utils import screaming_snake_case_to_pascal_case, snake_to_pascal_case

logger = logging.getLogger(__name__)


T = TypeVar("T")

TModel = TypeVar("TModel", bound=BaseModel)


class CustomGenerateJsonSchema(GenerateJsonSchema):
    """Custom JSON Schema generator to modify the way certain schemas are generated."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nullable_as_oneof = kwargs.get("nullable_as_oneof", True)
        self.unions_as_oneof = kwargs.get("unions_as_oneof", True)
        self.render_x_enum_names = kwargs.get("render_x_enum_names", True)

    def nullable_schema(self, schema: core_schema.NullableSchema) -> JsonSchemaValue:
        null_schema = {"type": "null"}
        inner_json_schema = self.generate_inner(schema["schema"])

        if inner_json_schema == null_schema:
            return null_schema
        else:
            if self.nullable_as_oneof:
                return self.get_flattened_oneof([inner_json_schema, null_schema])
            else:
                return super().get_flattened_anyof([inner_json_schema, null_schema])

    def get_flattened_oneof(self, schemas: list[JsonSchemaValue]) -> JsonSchemaValue:
        members = []
        for schema in schemas:
            if len(schema) == 1 and "oneOf" in schema:
                members.extend(schema["oneOf"])
            else:
                members.append(schema)
        members = _deduplicate_schemas(members)
        if len(members) == 1:
            return members[0]
        return {"oneOf": members}

    def enum_schema(self, schema: core_schema.EnumSchema) -> JsonSchemaValue:
        """Generates a JSON schema that matches an Enum value.

        Args:
            schema: The core schema.

        Returns:
            The generated JSON schema.
        """
        enum_type = schema["cls"]
        description = None if not enum_type.__doc__ else inspect.cleandoc(enum_type.__doc__)
        if (
            description == "An enumeration."
        ):  # This is the default value provided by enum.EnumMeta.__new__; don't use it
            description = None
        result: dict[str, Any] = {"title": enum_type.__name__, "description": description}
        result = {k: v for k, v in result.items() if v is not None}

        expected = [to_jsonable_python(v.value) for v in schema["members"]]

        result["enum"] = expected
        if len(expected) == 1:
            result["const"] = expected[0]

        types = {type(e) for e in expected}
        if isinstance(enum_type, str) or types == {str}:
            result["type"] = "string"
        elif isinstance(enum_type, int) or types == {int}:
            result["type"] = "integer"
        elif isinstance(enum_type, float) or types == {float}:
            result["type"] = "numeric"
        elif types == {bool}:
            result["type"] = "boolean"
        elif types == {list}:
            result["type"] = "array"

        _type = result.get("type", None)
        if (self.render_x_enum_names) and (_type != "string"):
            result["x-enumNames"] = [screaming_snake_case_to_pascal_case(v.name) for v in schema["members"]]

        return result

    def literal_schema(self, schema: core_schema.LiteralSchema) -> JsonSchemaValue:
        """Generates a JSON schema that matches a literal value.

        Args:
            schema: The core schema.

        Returns:
            The generated JSON schema.
        """
        expected = [v.value if isinstance(v, Enum) else v for v in schema["expected"]]
        # jsonify the expected values
        expected = [to_jsonable_python(v) for v in expected]

        types = {type(e) for e in expected}

        if len(expected) == 1:
            if isinstance(expected[0], str):
                return {"const": expected[0], "type": "string"}
            elif isinstance(expected[0], int):
                return {"const": expected[0], "type": "integer"}
            elif isinstance(expected[0], float):
                return {"const": expected[0], "type": "number"}
            elif isinstance(expected[0], bool):
                return {"const": expected[0], "type": "boolean"}
            elif isinstance(expected[0], list):
                return {"const": expected[0], "type": "array"}
            elif expected[0] is None:
                return {"const": expected[0], "type": "null"}
            else:
                return {"const": expected[0]}

        if types == {str}:
            return {"enum": expected, "type": "string"}
        elif types == {int}:
            return {"enum": expected, "type": "integer"}
        elif types == {float}:
            return {"enum": expected, "type": "number"}
        elif types == {bool}:
            return {"enum": expected, "type": "boolean"}
        elif types == {list}:
            return {"enum": expected, "type": "array"}
        # there is not None case because if it's mixed it hits the final `else`
        # if it's a single Literal[None] then it becomes a `const` schema above
        else:
            return {"enum": expected}

    def union_schema(self, schema: core_schema.UnionSchema) -> JsonSchemaValue:
        """Generates a JSON schema that matches a schema that allows values matching any of the given schemas.

        Args:
            schema: The core schema.

        Returns:
            The generated JSON schema.
        """
        generated: list[JsonSchemaValue] = []

        choices = schema["choices"]
        for choice in choices:
            # choice will be a tuple if an explicit label was provided
            choice_schema = choice[0] if isinstance(choice, tuple) else choice
            try:
                generated.append(self.generate_inner(choice_schema))
            except PydanticOmit:
                continue
            except PydanticInvalidForJsonSchema as exc:
                self.emit_warning("skipped-choice", exc.message)
        if len(generated) == 1:
            return generated[0]
        if self.unions_as_oneof is True:
            return self.get_flattened_oneof(generated)
        else:
            return self.get_flattened_anyof(generated)


TModel = TypeVar("TModel", bound=BaseModel)


def export_schema(
    model: Type[BaseModel],
    schema_generator: Type[GenerateJsonSchema] = CustomGenerateJsonSchema,
    mode: JsonSchemaMode = "serialization",
    remove_root: bool = True,
):
    """Export the schema of a model to a json file"""
    _model = model.model_json_schema(schema_generator=schema_generator, mode=mode)
    if remove_root:
        for to_remove in ["title", "description", "properties", "required", "type", "oneOf"]:
            _model.pop(to_remove, None)
    return json.dumps(_model, indent=2)


class BonsaiSgenSerializers(Enum):
    NONE = "None"
    JSON = "json"
    YAML = "yaml"


def bonsai_sgen(
    schema_path: PathLike,
    output_path: PathLike,
    namespace: Optional[str] = None,
    root_element: Optional[str] = None,
    serializer: Optional[List[BonsaiSgenSerializers]] = None,
) -> CompletedProcess:
    """Runs Bonsai.SGen to generate a Bonsai-compatible schema from a json-schema model
    For more information run `bonsai.sgen --help` in the command line.

    Returns:
        CompletedProcess: The result of running the command.
    Args:
        schema_path (PathLike): Target Json Schema file
        output_path (PathLike): Specifies the name of the
          file containing the generated code.
        namespace (Optional[str], optional): Specifies the
          namespace to use for all generated serialization
          classes. Defaults to DataSchema.
        root_element (Optional[str], optional):  Specifies the
          name of the class used to represent the schema root element.
          If None, it will use the json schema root element. Defaults to None.
        serializer (Optional[List[BonsaiSgenSerializers]], optional):
          Specifies the serializer data annotations to include in the generated classes.
          Defaults to None.
    """

    if serializer is None:
        serializer = [BonsaiSgenSerializers.JSON]

    _restore_cmd = run("dotnet tool restore", shell=True, check=True, capture_output=True)
    try:
        _restore_cmd.check_returncode()
    except CalledProcessError as e:
        print(f"Error occurred while restoring tools: {e}")
        print(
            "Ensure you have the Bonsai.Sgen tool installed locally. See https://github.com/bonsai-rx/sgen?tab=readme-ov-file#getting-started for instructions."
        )
        raise

    version = _check_bonsai_sgen_version()
    if version < Version.parse("0.6.0"):
        raise RuntimeError("Version of Bonsai.Sgen must be at least 0.6.0, found: " + str(version))

    cmd_string = (
        f'dotnet tool run bonsai.sgen "{schema_path}" -o "{Path(output_path).parent}" -n {Path(output_path).name}'
    )
    cmd_string += f" --namespace {namespace}" if namespace is not None else ""
    cmd_string += f" --root {root_element}" if root_element is not None else ""

    if len(serializer) == 0 or BonsaiSgenSerializers.NONE in serializer:
        cmd_string += " --serializer none"
    else:
        cmd_string += " --serializer"
        cmd_string += " ".join([f" {sr.value}" for sr in serializer])
    return run(cmd_string, shell=True, check=True)


def _check_bonsai_sgen_version() -> Version:
    """Check the version of the Bonsai.SGen tool."""
    result = run("dotnet tool run bonsai.sgen --version", shell=True, check=True, capture_output=True)
    version_str = result.stdout.strip()
    return Version.parse(version_str)


def convert_pydantic_to_bonsai(
    model: Type[BaseModel],
    *,
    model_name: Optional[str] = None,
    json_schema_output_dir: PathLike = Path("./src/DataSchemas/"),
    cs_output_dir: Optional[PathLike] = Path("./src/Extensions/"),
    cs_namespace: str = "DataSchema",
    cs_serializer: Optional[List[BonsaiSgenSerializers]] = None,
    json_schema_export_kwargs: Optional[Dict[str, Any]] = None,
    root_element: Optional[str] = None,
) -> Optional[CompletedProcess]:
    def _write_json(schema_path: PathLike, output_model_name: str, model: Type[BaseModel], **extra_kwargs) -> None:
        with open(os.path.join(schema_path, f"{output_model_name}.json"), "w", encoding="utf-8") as f:
            json_model = export_schema(model, **extra_kwargs)
            f.write(json_model)

    _model_name = model_name or model.__name__
    _write_json(json_schema_output_dir, _model_name, model, **(json_schema_export_kwargs or {}))

    if cs_output_dir is not None:
        cmd_return = bonsai_sgen(
            schema_path=Path(os.path.join(json_schema_output_dir, f"{_model_name}.json")),
            output_path=Path(os.path.join(cs_output_dir, f"{snake_to_pascal_case(_model_name)}.Generated.cs")),
            namespace=cs_namespace,
            serializer=cs_serializer,
            root_element=root_element,
        )
        return cmd_return

    return None
