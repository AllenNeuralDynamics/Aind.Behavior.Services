from enum import StrEnum
from typing import Any, Generic, Literal, Optional, TypeVar

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, SerializeAsAny

from aind_behavior_services import __semver__
from aind_behavior_services.base import SchemaVersionedModel

from .schema import SgenNamespace

_sgen_namespace = SgenNamespace("AllenNeuralDynamics.AindBehaviorServices.DataTypes")


@_sgen_namespace.sgen_typename()
class DataType(StrEnum):
    STRING = "string"
    NUMBER = "number"
    OBJECT = "object"
    ARRAY = "array"
    NULL = "null"
    BOOLEAN = "boolean"


@_sgen_namespace.sgen_typename()
class TimestampSource(StrEnum):
    NULL = "null"
    HARP = "harp"
    RENDER = "render"


TData = TypeVar("TData", bound=Any)


@_sgen_namespace.sgen_typename()
class SoftwareEvent(BaseModel, Generic[TData]):
    """
    A software event is a generic event that can be used to track any event that occurs in the software.
    """

    name: str = Field(description="The name of the event")
    timestamp: Optional[float] = Field(default=None, description="The timestamp of the event")
    timestamp_source: TimestampSource = Field(default=TimestampSource.NULL, description="The source of the timestamp")
    frame_index: Optional[int] = Field(default=None, ge=0, description="The frame index of the event")
    frame_timestamp: Optional[float] = Field(default=None, description="The timestamp of the frame")
    data: SerializeAsAny[Optional[TData]] = Field(default=None, description="The data of the event")
    data_type: DataType = Field(default=DataType.NULL, description="The data type of the event")
    data_type_hint: Optional[str] = Field(default=None, description="The data type hint of the event")


@_sgen_namespace.sgen_typename()
class RenderSynchState(BaseModel):
    sync_quad_value: Optional[float] = Field(default=None, ge=0, le=1, description="The synchronization quad value")
    frame_index: Optional[int] = Field(default=None, ge=0, description="The frame index of the event")
    frame_timestamp: Optional[float] = Field(default=None, ge=0, description="The timestamp of the frame")


@_sgen_namespace.sgen_typename()
class StartExperimentPayload(BaseModel):
    timestamp: AwareDatetime = Field(description="The start time of the session")


@_sgen_namespace.sgen_typename()
class EndExperimentPayload(BaseModel):
    timestamp: AwareDatetime = Field(description="The end time of the session")


class DataTypes(SchemaVersionedModel):
    version: Literal[__semver__] = __semver__
    software_event: SoftwareEvent
    render_synch_state: RenderSynchState
    start_payload: StartExperimentPayload
    end_payload: EndExperimentPayload
    model_config = ConfigDict(
        json_schema_extra={
            "x-abstract": "True",
        }
    )
