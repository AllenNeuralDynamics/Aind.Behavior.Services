import unittest
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, RootModel, TypeAdapter

from aind_behavior_services.schema import sgen_typename


class SchemaTests(unittest.TestCase):
    """tests for schema generation"""

    def test_sgen_typename_decorator(self):

        @sgen_typename(typename="OpenTK.Vector2")
        class Vector2(BaseModel):
            x: float
            y: float

        @sgen_typename(typename="System.Int")
        class IntRootModel(RootModel[int]):
            root: int

        self.assertEqual(Vector2.model_json_schema()["x-sgen-typename"], "OpenTK.Vector2")
        self.assertEqual(IntRootModel.model_json_schema()["x-sgen-typename"], "System.Int")

    def test_sgen_typename_deep_chain_strips_typename(self):
        """x-sgen-typename must not bleed through multiple levels of plain subclasses."""

        @sgen_typename(typename="OpenTK.Vector2")
        class Vector2(BaseModel):
            x: float
            y: float

        class Vector3(Vector2):
            z: float

        class Vector4(Vector3):
            w: float

        self.assertNotIn("x-sgen-typename", Vector3.model_json_schema())
        self.assertNotIn("x-sgen-typename", Vector4.model_json_schema())

    def test_sgen_typename_original_class_not_mutated(self):
        """The decorator must not modify the original (undecorated) class."""

        class MyModel(BaseModel):
            x: float

        decorated = sgen_typename(typename="Foo.Bar")(MyModel)

        self.assertNotIn("x-sgen-typename", MyModel.model_json_schema())
        self.assertEqual(decorated.model_json_schema()["x-sgen-typename"], "Foo.Bar")

    def test_sgen_typename_preserves_existing_json_schema_extra(self):
        """Existing json_schema_extra keys must be kept alongside x-sgen-typename."""

        class MyModel(BaseModel):
            model_config = ConfigDict(json_schema_extra={"x-custom": "hello"})
            x: float

        decorated = sgen_typename(typename="Foo.Bar")(MyModel)
        schema = decorated.model_json_schema()

        self.assertEqual(schema["x-sgen-typename"], "Foo.Bar")
        self.assertEqual(schema["x-custom"], "hello")

    def test_sgen_typename_redecorate_updates_value(self):
        """Re-applying the decorator to an already-decorated class replaces the typename."""

        @sgen_typename(typename="Foo.First")
        class MyModel(BaseModel):
            x: float

        @sgen_typename(typename="Foo.Second")
        class Renamed(MyModel):
            pass

        self.assertEqual(MyModel.model_json_schema()["x-sgen-typename"], "Foo.First")
        self.assertEqual(Renamed.model_json_schema()["x-sgen-typename"], "Foo.Second")

        Renamed = sgen_typename(typename="Foo.Second")(MyModel)
        self.assertEqual(MyModel.model_json_schema()["x-sgen-typename"], "Foo.First")
        self.assertEqual(Renamed.model_json_schema()["x-sgen-typename"], "Foo.Second")

    def test_sgen_typename_non_basemodel_annotated(self):
        """Non-BaseModel types (e.g. Enum) use the Annotated path; typename appears on the field reference."""

        @sgen_typename(typename="My.FooEnum")
        class FooEnum(StrEnum):
            A = "A"
            B = "B"

        class Container(BaseModel):
            val: FooEnum

        schema = Container.model_json_schema()
        self.assertEqual(schema["properties"]["val"]["x-sgen-typename"], "My.FooEnum")

    def test_sgen_typename_as_annotated_true(self):
        """as_annotated=True forces the Annotated path even for BaseModel subclasses; typename appears on the field reference."""

        @sgen_typename(typename="My.FooModel", as_annotated=True)
        class FooModel(BaseModel):
            x: float

        class Container(BaseModel):
            val: FooModel

        schema = Container.model_json_schema()
        self.assertEqual(schema["properties"]["val"]["x-sgen-typename"], "My.FooModel")

    def test_sgen_typename_as_annotated_does_not_mutate_defs(self):
        """as_annotated=True must not place the typename inside $defs, only on the field reference."""

        @sgen_typename(typename="My.FooModel", as_annotated=True)
        class FooModel(BaseModel):
            x: float

        class Container(BaseModel):
            val: FooModel

        schema = Container.model_json_schema()
        self.assertNotIn("x-sgen-typename", schema.get("$defs", {}).get("FooModel", {}))

    def test_sgen_typename_non_basemodel_does_not_mutate_defs(self):
        """Enum typename must not appear inside $defs, only on the field reference."""

        @sgen_typename(typename="My.FooEnum")
        class FooEnum(StrEnum):
            A = "A"
            B = "B"

        class Container(BaseModel):
            val: FooEnum

        schema = Container.model_json_schema()
        self.assertNotIn("x-sgen-typename", schema.get("$defs", {}).get("FooEnum", {}))

    def test_sgen_typename_as_annotated_preserves_class_identity(self):
        """as_annotated=True must not create a new subclass; the original class is returned unchanged so isinstance checks and pattern matching still work."""

        class FooModel(BaseModel):
            x: float

        decorated = sgen_typename(typename="My.FooModel", as_annotated=True)(FooModel)

        self.assertNotIn("x-sgen-typename", decorated.model_json_schema())

        # According to pydantic docs, the TypeAdapter should propagate the json-extra
        adapter_schema = TypeAdapter(decorated)
        self.assertIn("x-sgen-typename", adapter_schema.json_schema())
