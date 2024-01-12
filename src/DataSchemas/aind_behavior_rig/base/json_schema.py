
from pydantic.json_schema import (
    GenerateJsonSchema,
    JsonSchemaValue,
    _deduplicate_schemas,
)
from pydantic_core import core_schema
from pydantic import BaseModel
from os import PathLike
from typing import TypeVar


REF_TEMPLATE = "#/definitions/{model}"


class CustomGenerateJsonSchema(GenerateJsonSchema):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nullable_as_oneof = kwargs.get("nullable_as_oneof", True)
        self.ref_template = kwargs.get("ref_template", REF_TEMPLATE)

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


Model = TypeVar("Model", bound=BaseModel)


def export_schema(model: Model,
                  output_path: PathLike,
                  schema_generator: GenerateJsonSchema = CustomGenerateJsonSchema):
    """Export the schema of a model to a json file"""
    return model.model_json_schema(schema_generator=schema_generator)