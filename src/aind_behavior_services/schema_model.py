from bonsai.sgen import SchemaModel as _SchemaModel
from pydantic import ConfigDict


class SchemaModel(_SchemaModel):
    """`bonsai.sgen.SchemaModel` that keeps snake_case keys instead of the upstream camelCase aliases."""

    model_config = ConfigDict(alias_generator=None, validate_by_name=True, serialize_by_alias=False)
