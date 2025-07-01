import enum
from typing import Annotated, Any, Dict, Generic, Literal, Optional, Type, TypeVar, Union, cast

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, RootModel, SerializeAsAny, create_model

__version__ = "0.0.1"
PROTOCOL_VERSION = __version__.split(".")[0]

TPayload = TypeVar("TPayload", bound=Any)


class MessageType(enum.StrEnum):
    """
    Enumeration of possible message types in the protocol.

    Examples:
        ```python
        MessageType.REQUEST  # 'request'
        MessageType.REPLY    # 'reply'
        MessageType.EVENT    # 'event'
        ```
    """

    REQUEST = "request"
    REPLY = "reply"
    EVENT = "event"


class Message(BaseModel, Generic[TPayload]):
    """
    A generic message container that can carry any payload type.
    While not marked as abstract, it is intended to be subclassed
    for specific message types with defined payloads.

    Args:
        cls_type: The specific message class type identifier (discriminator)
        message_type: The category of message (request, reply, or event)
        protocol_version: The major version of the message protocol being used
        timestamp: When the message was created
        payload: The actual message content
        process_id: Identifier of the process (e.g.: executable) that created the message
        hostname: Name of the host machine that created the message
        rig_name: Name of the experimental rig that created the message
    """

    cls_type: str = "Message"
    message_type: MessageType
    protocol_version: Literal[PROTOCOL_VERSION] = PROTOCOL_VERSION
    timestamp: Optional[AwareDatetime] = Field(description="The timestamp of the message")
    payload: SerializeAsAny[TPayload] = Field(description="The payload of the message")
    process_id: Optional[str] = Field(description="Process that created the message")
    hostname: Optional[str] = Field(description="Hostname that created the message")
    rig_name: Optional[str] = Field(description="Rig name that created the message")


class MessageProtocolBuilder:
    """
    A builder class for creating message protocols with registered payload types.

    This class allows you to register payload classes using a decorator pattern
    and then generate a complete message protocol that includes all registered
    payload types with proper discriminated union support.

    Examples:
        ```python
        builder = MessageProtocolBuilder()

        # Register a payload class using the decorator
        @builder.register
        class MyPayload(BaseModel):
            data: str

        # Register a payload with function syntax
        builder.register(MyPayload, override_name="CustomMessage")

        protocol_type = builder.create_message_protocol()
        # Now you can use protocol_type for validation
        ```
    """

    def __init__(self):
        """
        Initialize a new MessageProtocolBuilder instance.

        Creates an empty registry for payload types that will be populated
        using the register decorator.
        """
        self._registered_payloads: Dict[str, Type[Any]] = {}

    def register(self, payload_class: Type[TPayload], override_name: Optional[str] = None) -> Type[TPayload]:
        """
        Decorator to register a payload class with the protocol builder.

        This method can be used as a decorator to automatically register
        payload classes. The class name will be sanitized by replacing
        'Payload' with 'Message' unless an override name is provided.

        Args:
            payload_class: The payload class to register
            override_name: Optional custom name for the message type

        Returns:
            The same payload class (for use as decorator)

        Raises:
            ValueError: If a payload with the same name is already registered

        Examples:
            ```python
            builder = MessageProtocolBuilder()

            @builder.register
            class StatusPayload(BaseModel):
                status: str

            @builder.register(override_name="CustomStatus")
            class AnotherPayload(BaseModel):
                value: int

            builder.register(
                AnotherPayload, override_name="CustomData")
            ```
        """

        def _sanitize_payload_name(payload_name: str) -> str:
            return payload_name.replace("Payload", "Message")

        cls_name = override_name or _sanitize_payload_name(payload_class.__name__)
        if cls_name in self._registered_payloads:
            raise ValueError(f"Payload class '{cls_name}' is already registered. Use a different name or override.")
        self._registered_payloads[cls_name] = payload_class
        return payload_class

    @staticmethod
    def _register_payload(
        payload: Type[TPayload],
        name: str,
    ) -> Type[Message[TPayload]]:
        return create_model(
            name,
            cls_type=(Literal[name], Field(default=name)),
            payload=(payload, Field(description=f"The payload for {name}.")),
            __base__=Message[TPayload],
        )

    def create_message_protocol(self, model_name: str = "RegisteredMessage") -> Type[RootModel[Message]]:
        """
        Creates a discriminated union type from all registered payloads.

        This method generates a Pydantic RootModel that can validate and serialize
        any of the registered message types using discriminated unions based
        on the cls_type field.

        Args:
            model_name: Name for the generated protocol model

        Returns:
            A RootModel type that can handle all registered message types

        Raises:
            ValueError: If no payloads have been registered

        Examples:
            ```python
            builder = MessageProtocolBuilder()

            @builder.register
            class StatusPayload(BaseModel):
                status: str

            @builder.register
            class DataPayload(BaseModel):
                values: List[int]

            ProtocolType = builder.create_message_protocol()
            # ProtocolType can now validate StatusMessage or DataMessage instances
            ```
        """
        if not self._registered_payloads:
            raise ValueError("No payloads have been registered. Use the @register decorator on payload classes.")

        registered_message_types = tuple(
            self._register_payload(payload, name) for name, payload in self._registered_payloads.items()
        )

        _t = create_model(
            model_name,
            __base__=RootModel[
                Annotated[
                    Union[registered_message_types],
                    Field(discriminator="cls_type"),
                ]
            ],
            __config__=ConfigDict(json_schema_extra={"x-abstract": True}),
        )

        return cast(
            Type[RootModel[Message]],
            _t,
        )


protocol = MessageProtocolBuilder()


class LogLevel(enum.IntEnum):
    """
    Enumeration of log levels for the logging system.

    Follows standard Python logging levels with integer values
    that allow for easy comparison and filtering.

    Examples:
        ```python
        LogLevel.ERROR > LogLevel.WARNING  # True
        LogLevel.DEBUG.value               # 10
        str(LogLevel.INFO)                 # 'LogLevel.INFO'
        ```
    """

    CRITICAL = 50
    ERROR = 40
    WARNING = 30
    INFO = 20
    DEBUG = 10
    NOTSET = 0


@protocol.register
class LogPayload(BaseModel):
    """
    Payload for log messages containing logging information.

    This payload carries log data including the message content,
    severity level, optional context, and application version.

    Attributes:
        message: The actual log message text
        level: Severity level of the log entry
        context: Optional additional data related to the log
        application_version: Version of the application generating the log

    Examples:
        ```python
        log_payload = LogPayload(
            message="System startup complete",
            level=LogLevel.INFO,
            context={"operator": "John Doe"},
            application_version="1.0.0"
        )
        print(log_payload.level)  # LogLevel.INFO
        ```
    """

    message: str = Field(description="The message of the log")
    level: LogLevel = Field(default=LogLevel.DEBUG, description="The level of the log message")
    context: Optional[SerializeAsAny[Any]] = Field(default=None, description="Additional context for the log message")
    application_version: Optional[str] = Field(default=None, description="The version of the application")


class HeartbeatStatus(enum.IntEnum):
    """
    Enumeration of possible heartbeat status values.

    Represents the health status of a system component,
    with higher values indicating more severe issues.

    Examples:
        ```python
        HeartbeatStatus.OK                            # <HeartbeatStatus.OK: 0>
        HeartbeatStatus.CRITICAL > HeartbeatStatus.WARNING  # True
        int(HeartbeatStatus.ERROR)                    # 2
        ```
    """

    OK = 0
    WARNING = 1
    ERROR = 2
    CRITICAL = 3


@protocol.register
class HeartbeatPayload(BaseModel):
    """
    Payload for heartbeat messages indicating system health status.

    Heartbeat messages are used to monitor the health and availability
    of system components. They include a status indicator and optional
    context information.

    Attributes:
        context: Optional additional data about the system state
        status: Current health status of the component

    Examples:
        ```python
        heartbeat = HeartbeatPayload(
            status=HeartbeatStatus.OK,
            context={"cpu_usage": 0.25, "memory_usage": 0.60}
        )
        print(heartbeat.status)  # HeartbeatStatus.OK

        warning_heartbeat = HeartbeatPayload(
            status=HeartbeatStatus.WARNING,
            context={"disk_space_low": True}
        )
        ```
    """

    context: SerializeAsAny[Optional[Any]] = Field(
        default=None, description="Additional context for the heartbeat message."
    )
    status: HeartbeatStatus = Field(description="The status of the heartbeat message")


RegisteredMessages: Type = protocol.create_message_protocol()


class MessageProtocol(BaseModel):
    """
    Container for the complete message protocol including all registered message types.

    """

    model_config = ConfigDict(json_schema_extra={"x-abstract": True})
    registered_message: RegisteredMessages  # type: ignore
    message: Message
