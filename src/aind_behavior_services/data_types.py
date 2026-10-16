from enum import StrEnum
from typing import Any, Generic, TypeVar

from bonsai.sgen import SchemaEnum
from pydantic import AwareDatetime, Field, SerializeAsAny

from aind_behavior_services.schema_model import SchemaModel

SGEN_NAMESPACE = "AllenNeuralDynamics.AindBehaviorServices.DataTypes"


class DataType(SchemaEnum, StrEnum):
    STRING = "string"
    NUMBER = "number"
    OBJECT = "object"
    ARRAY = "array"
    NULL = "null"
    BOOLEAN = "boolean"


class TimestampSource(SchemaEnum, StrEnum):
    NULL = "null"
    HARP = "harp"
    RENDER = "render"


TData = TypeVar("TData", bound=Any)


class SoftwareEvent(SchemaModel, Generic[TData]):
    """
    A software event is a generic event that can be used to track any event that occurs in the software.
    """

    name: str = Field(description="The name of the event")
    timestamp: float | None = Field(default=None, description="The timestamp of the event")
    timestamp_source: TimestampSource = Field(default=TimestampSource.NULL, description="The source of the timestamp")
    frame_index: int | None = Field(default=None, ge=0, description="The frame index of the event")
    frame_timestamp: float | None = Field(default=None, description="The timestamp of the frame")
    data: SerializeAsAny[TData | None] = Field(default=None, description="The data of the event")
    data_type: DataType = Field(default=DataType.NULL, description="The data type of the event")
    data_type_hint: str | None = Field(default=None, description="The data type hint of the event")


class _SoftwareEvent(SoftwareEvent[Any], sgen_typename=f"{SGEN_NAMESPACE}.SoftwareEvent"):
    """Concrete form of `SoftwareEvent` for schema export, since generic models cannot be exported."""


class RenderSynchState(SchemaModel):
    sync_quad_value: float | None = Field(default=None, ge=0, le=1, description="The synchronization quad value")
    frame_index: int | None = Field(default=None, ge=0, description="The frame index of the event")
    frame_timestamp: float | None = Field(default=None, ge=0, description="The timestamp of the frame")


class StartExperimentPayload(SchemaModel):
    timestamp: AwareDatetime = Field(description="The start time of the session")


class EndExperimentPayload(SchemaModel):
    timestamp: AwareDatetime = Field(description="The end time of the session")
