from enum import StrEnum
from typing import Any, Generic, Literal, Optional, TypeVar

from pydantic import BaseModel, ConfigDict, Field, field_validator

from aind_behavior_services import __semver__
from aind_behavior_services.base import SchemaVersionedModel


class DataType(StrEnum):
    STRING = "string"
    NUMBER = "number"
    BOOLEAL = "boolean"  # For backward compatibility
    OBJECT = "object"
    ARRAY = "array"
    NULL = "null"
    BOOLEAN = "boolean"


class TimestampSource(StrEnum):
    NULL = "null"
    HARP = "harp"
    RENDER = "render"


TData = TypeVar("TData", bound=Any)


class SoftwareEvent(BaseModel, Generic[TData]):
    """
    A software event is a generic event that can be used to track any event that occurs in the software.
    """

    name: str = Field(..., description="The name of the event")
    timestamp: Optional[float] = Field(default=None, description="The timestamp of the event")
    timestamp_source: TimestampSource = Field(default=TimestampSource.NULL, description="The source of the timestamp")
    frame_index: Optional[int] = Field(default=None, ge=0, description="The frame index of the event")
    frame_timestamp: Optional[float] = Field(default=None, description="The timestamp of the frame")
    data: Optional[TData] = Field(default=None, description="The data of the event")
    data_type: DataType = Field(default=DataType.NULL, description="The data type of the event")
    data_type_hint: Optional[str] = Field(default=None, description="The data type hint of the event")

    @field_validator("data_type", mode="after")
    @classmethod
    def _fix_typoed_boolean(cls, v: DataType) -> DataType:
        if v == DataType.BOOLEAL:
            return DataType.BOOLEAN
        return v


class RenderSynchState(BaseModel):
    sync_quad_value: Optional[float] = Field(default=None, ge=0, le=1, description="The synchronization quad value")
    frame_index: Optional[int] = Field(default=None, ge=0, description="The frame index of the event")
    frame_timestamp: Optional[float] = Field(default=None, ge=0, description="The timestamp of the frame")


class DataTypes(SchemaVersionedModel):
    version: Literal[__semver__] = __semver__
    software_event: SoftwareEvent
    render_synch_state: RenderSynchState
    model_config = ConfigDict(
        json_schema_extra={
            "x-abstract": "True",
        }
    )
