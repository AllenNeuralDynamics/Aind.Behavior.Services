import datetime
import logging
from typing import (
    TYPE_CHECKING,
    Annotated,
    Any,
    Literal,
    get_args,
    get_origin,
)

from aind_behavior_curriculum.task import SEMVER_REGEX
from pydantic import (
    AwareDatetime,
    BaseModel,
    Field,
    ValidatorFunctionWrapHandler,
    WrapValidator,
    field_validator,
)
from pydantic_core import PydanticUndefined
from semver import Version

from aind_behavior_services import __semver__

logger = logging.getLogger(__name__)


class SchemaVersionedModel(BaseModel):
    aind_behavior_services_pkg_version: Literal[__semver__] = Field(
        default=__semver__, pattern=SEMVER_REGEX, title="aind_behavior_services package version", frozen=True
    )
    version: str = Field(..., pattern=SEMVER_REGEX, description="schema version", title="Version", frozen=True)

    @field_validator("aind_behavior_services_pkg_version", "version", mode="before", check_fields=False)
    @classmethod
    def coerce_version(cls, v: str, ctx) -> str:
        return coerce_schema_version(cls, v, ctx.field_name)


def coerce_schema_version(cls: type[BaseModel], v: str, version_string: str = "version") -> str:
    semver = Version.parse(v)

    _default_schema_version: Version | None = None

    try:  # Get the default schema version from the model literal field
        annotation = cls.model_fields[version_string].annotation
        if get_origin(annotation) is Literal:
            _default_schema_version = Version.parse(get_args(annotation)[0])
    except IndexError:  # This handles the case where the base class does not define a literal schema_version value
        return v

    if _default_schema_version is None:  # Fallback to getting the default value from the field
        default = cls.model_fields[version_string].default
        if default is PydanticUndefined:
            return v
        else:
            _default_schema_version = Version.parse(cls.model_fields[version_string].default)

    assert _default_schema_version is not None

    if semver != _default_schema_version:
        logger.warning(
            "Deserialized versioned field %s, expected %s. Will attempt to coerce. "
            "This will be considered a best-effort operation.",
            semver,
            _default_schema_version,
        )
    return str(_default_schema_version)


if TYPE_CHECKING:
    DefaultAwareDatetime = Annotated[AwareDatetime, ...]
else:

    def _add_default_tz(dt: Any, handler: ValidatorFunctionWrapHandler) -> datetime.datetime:
        if isinstance(dt, str):
            dt = datetime.datetime.fromisoformat(dt)
        if isinstance(dt, datetime.datetime):
            if dt.tzinfo is None:
                dt = dt.astimezone()
        return dt

    DefaultAwareDatetime = Annotated[AwareDatetime, WrapValidator(_add_default_tz), Field(validate_default=True)]
