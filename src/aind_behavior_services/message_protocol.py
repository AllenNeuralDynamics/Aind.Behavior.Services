import enum
from typing import Annotated, Any, Generic, Literal, Optional, TypeVar, Union, ClassVar, cast

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, RootModel, SerializeAsAny, Tag, Discriminator, computed_field, TypeAdapter, create_model
from pydantic.fields import FieldInfo
from typing import Type
from typing_extensions import TypeAliasType
from typing import get_args
import abc

__version__ = "0.0.1"
PROTOCOL_VERSION = __version__.split(".")[0]

class MessageType(enum.StrEnum):
    REQUEST = "request"
    REPLY = "reply"
    EVENT = "event"


class BasePayload(abc.ABC, BaseModel):
    cls_type: str

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls_name = cls.__name__
        cls.__annotations__["cls_type"] = Literal[cls_name]
        cls.cls_type = cls_name



TPayload = TypeVar("TPayload", bound=Annotated[BasePayload, Field(json_schema_extra={"x-abstract": True})] | Any)


class Message(BaseModel, Generic[TPayload]):
    """
    A message is a generic message that can be used to track any message that occurs in the software.
    """
    message_type: MessageType
    protocol_version: Literal[PROTOCOL_VERSION] = PROTOCOL_VERSION
    timestamp: AwareDatetime = Field(description="The timestamp of the message")
    payload: SerializeAsAny[TPayload] = Field(description="The payload of the message")
    process_id: str = Field(description="Process that created the message")
    hostname: str = Field(description="Hostname that created the message")
    rig_name: str = Field(description="Rig name that created the message")

    @classmethod
    def model_parametrized_name(cls, params: tuple[type[Any], ...]) -> str:
        return f'{params[0].__name__.title()}Message'
    
    


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


class LogPayload(BasePayload):
    """
    A payload for a log message.
    """

    message: str = Field(description="The message of the log")
    level: LogLevel = Field(default=LogLevel.DEBUG, description="The level of the log message")
    context: Optional[SerializeAsAny[Any]] = Field(default=None, description="Additional context for the log message")
    application_version: Optional[str] = Field(default=None, description="The version of the application")


class HeartbeatStatus(enum.IntEnum):

    OK = 0
    WARNING = 1
    ERROR = 2
    CRITICAL = 3


class HeartbeatPayload(BasePayload):
    """
    A payload for a heartbeat message.
    """

    context: SerializeAsAny[Optional[Any]] = Field(default=None, description="Additional context for the heartbeat message.")
    status: HeartbeatStatus = Field(description="The status of the heartbeat message")


class StopPayload(BasePayload):
    """
    A payload for a stop message.
    """

    args: SerializeAsAny[Optional[Any]] = Field(default=None, description="Arguments for the stop message")


class StartPayload(BasePayload):
    """
    A payload for a start message.
    """

    args: SerializeAsAny[Optional[Any]] = Field(default=None, description="Arguments for the start message")


Payload = TypeAliasType(
    "Payload",
    Annotated[
        Union[
            StartPayload,
            LogPayload,
            StopPayload,
            HeartbeatPayload
        ],
        Field(discriminator="cls_type"),
    ],
)


# this is annoying. pydantic does not allow you to overload the keys generated in the compiled json-schema
# when using the Generics notation. A workaround is to use inheritance instead, and override the field;
class RegisteredMessage(Message[Payload]):
    model_config = ConfigDict(json_schema_extra={"x-abstract": True})
    payload: Payload = Field(description="The payload of the message")


class MessageProtocol(BaseModel):
    model_config = ConfigDict(json_schema_extra={"x-abstract": True})
    registered_message: RegisteredMessage
    message: Message
