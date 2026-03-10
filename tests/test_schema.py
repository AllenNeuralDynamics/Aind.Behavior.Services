import unittest

from pydantic import BaseModel, ConfigDict, RootModel

from aind_behavior_services.schema import sgen_typename


class SchemaTests(unittest.TestCase):
    """tests for schema generation"""

    def test_sgen_typename_decorator(self):

        @sgen_typename("OpenTK.Vector2")
        class Vector2(BaseModel):
            x: float
            y: float

        @sgen_typename("System.Int")
        class IntRootModel(RootModel[int]):
            root: int

        self.assertEqual(Vector2.model_json_schema()["x-sgen-typename"], "OpenTK.Vector2")
        self.assertEqual(IntRootModel.model_json_schema()["x-sgen-typename"], "System.Int")

    def test_sgen_typename_deep_chain_strips_typename(self):
        """x-sgen-typename must not bleed through multiple levels of plain subclasses."""

        @sgen_typename("OpenTK.Vector2")
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

        decorated = sgen_typename("Foo.Bar")(MyModel)

        self.assertNotIn("x-sgen-typename", MyModel.model_json_schema())
        self.assertEqual(decorated.model_json_schema()["x-sgen-typename"], "Foo.Bar")

    def test_sgen_typename_preserves_existing_json_schema_extra(self):
        """Existing json_schema_extra keys must be kept alongside x-sgen-typename."""

        class MyModel(BaseModel):
            model_config = ConfigDict(json_schema_extra={"x-custom": "hello"})
            x: float

        decorated = sgen_typename("Foo.Bar")(MyModel)
        schema = decorated.model_json_schema()

        self.assertEqual(schema["x-sgen-typename"], "Foo.Bar")
        self.assertEqual(schema["x-custom"], "hello")

    def test_sgen_typename_redecorate_updates_value(self):
        """Re-applying the decorator to an already-decorated class replaces the typename."""

        @sgen_typename("Foo.First")
        class MyModel(BaseModel):
            x: float

        @sgen_typename("Foo.Second")
        class Renamed(MyModel):
            pass

        self.assertEqual(MyModel.model_json_schema()["x-sgen-typename"], "Foo.First")
        self.assertEqual(Renamed.model_json_schema()["x-sgen-typename"], "Foo.Second")

        Renamed = sgen_typename("Foo.Second")(MyModel)
        self.assertEqual(MyModel.model_json_schema()["x-sgen-typename"], "Foo.First")
        self.assertEqual(Renamed.model_json_schema()["x-sgen-typename"], "Foo.Second")
