import enum
from typing import Annotated, Any, Generic, Literal, Optional, TypeVar, Union

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, RootModel, SerializeAsAny
from typing_extensions import TypeAliasType

TPayload = TypeVar("TPayload", bound=BaseModel)

__version__ = "0.0.1"
PROTOCOL_VERSION = __version__.split(".")[0]


class MessageType(enum.StrEnum):
    REQUEST = "request"
    REPLY = "reply"
    EVENT = "event"


class BaseMessage(BaseModel, Generic[TPayload]):
    """
    A message is a generic message that can be used to track any message that occurs in the software.
    """

    message_type: MessageType
    protocol_version: Literal[PROTOCOL_VERSION] = PROTOCOL_VERSION
    timestamp: AwareDatetime = Field(description="The timestamp of the message")
    payload: TPayload = Field(description="The payload of the message")
    process_id: str = Field(description="Process that created the message")
    hostname: str = Field(description="Hostname that created the message")
    rig_name: str = Field(description="Rig name that created the message")


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


class LogPayload(BaseModel):
    """
    A payload for a log message.
    """

    payload_type: Literal["log"] = "log"
    level: LogLevel = Field(LogLevel.DEBUG, description="The level of the log message")
    message: str = Field(description="The message of the log")
    context: SerializeAsAny[Any] = Field(description="Additional context for the log message")
    application_version: Optional[str] = Field(default=None, description="The version of the application")


class StopPayload(BaseModel):
    payload_type: Literal["stop"] = "stop"
    args: SerializeAsAny[Optional[Any]] = Field(default=None, description="Arguments for the stop message")


class StartPayload(BaseModel):
    payload_type: Literal["start"] = "start"
    args: SerializeAsAny[Optional[Any]] = Field(default=None, description="Arguments for the stop message")


Payload = TypeAliasType(
    "Payload",
    Annotated[
        Union[
            StartPayload,
            LogPayload,
            StopPayload,
        ],
        Field(discriminator="payload_type"),
    ],
)


class Message(RootModel):
    model_config = ConfigDict(title="Message", model_title_generator=lambda x: "RegisteredMessage")
    root: BaseMessage[Any]


class RegisteredMessage(RootModel):
    model_config = ConfigDict(title="RegisteredMessage", model_title_generator=lambda x: "RegisteredMessage")
    root: BaseMessage[Payload]


class MessageProtocol(BaseModel):
    model_config = ConfigDict(json_schema_extra={"x-abstract": "True"})
    any_message: Message
    known_message: RegisteredMessage
