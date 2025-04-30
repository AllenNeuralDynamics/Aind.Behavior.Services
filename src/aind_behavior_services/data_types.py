import datetime
import enum
import logging
from enum import StrEnum
from typing import Any, Generic, Literal, Optional, TypeVar, cast

from pydantic import BaseModel, Field, SerializeAsAny, create_model
from typing_extensions import Annotated, TypeAliasType, Union

from .base import SchemaVersionedModel

logger = logging.getLogger(__name__)

__version__ = "0.1.1"


class DataType(StrEnum):
    STRING = "string"
    NUMBER = "number"
    BOOLEAL = "boolean"
    OBJECT = "object"
    ARRAY = "array"
    NULL = "null"


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
    data_type: DataType = Field(default=DataType.NULL, alias="dataType", description="The data type of the event")
    data_type_hint: Optional[str] = Field(default=None, description="The data type hint of the event")


class RenderSynchState(BaseModel):
    sync_quad_value: Optional[float] = Field(default=None, ge=0, le=1, description="The synchronization quad value")
    frame_index: Optional[int] = Field(default=None, ge=0, description="The frame index of the event")
    frame_timestamp: Optional[float] = Field(default=None, ge=0, description="The timestamp of the frame")


TPayload = TypeVar("TPayload", bound=BaseModel)


def with_message_type(cls: type[TPayload]) -> type[TPayload]:
    name = cls.__name__
    literal_type = Literal[name]

    if "message_type" not in cls.__annotations__:
        new_model = create_model(
            name,
            __base__=cls,
            message_type=Annotated[literal_type, Field(default=name)],
        )
        return cast(cls, new_model)
    else:
        return cls


class MessageType(StrEnum):
    REQUEST = "request"
    REPLY = "reply"
    EVENT = "event"


class BaseMessage(BaseModel, Generic[TPayload]):
    """
    A message is a generic message that can be used to track any message that occurs in the software.
    """

    message_type: MessageType
    protocol_version: Literal[1] = 1
    timestamp: datetime.datetime = Field(description="The timestamp of the message")
    payload: TPayload = Field(description="The payload of the message")
    process_id: str = Field(description="Process that created the message")
    hostname: str = Field(description="Hostname that created the message")


class LogLevel(enum.IntEnum):
    """
    Log levels for the logging system.
    """

    CRITICAL = 50
    ERROR = 40
    WARNING = 30
    INFO = 20
    DEBUG = 10
    NOTSET = 0


@with_message_type
class LogPayload(BaseModel):
    """
    A payload for a log message.
    """

    level: LogLevel = Field(LogLevel.DEBUG, description="The level of the log message")
    message: SerializeAsAny[Any] = Field(..., description="The message of the log")
    application_version: Optional[str] = Field(default=None, description="The version of the application")


class StopPayload(BaseModel):
    message_type: Literal["stop"] = "stop"


@with_message_type
class StartPayload(BaseModel):
    pass


PayloadType = TypeAliasType(
    "PayloadType",
    Annotated[
        Union[
            StartPayload,
            LogPayload,
            StopPayload,
        ],
        Field(discriminator="message_type"),
    ],
)

message = BaseMessage[PayloadType]


class DataTypes(SchemaVersionedModel):
    version: Literal[__version__] = __version__
    software_event: SoftwareEvent
    render_synch_state: RenderSynchState
    # messages: MessageType
    # message: BaseMessage
    message_generic: BaseMessage[PayloadType]

    class Config:
        json_schema_extra = {
            "x-abstract": "True",
        }
