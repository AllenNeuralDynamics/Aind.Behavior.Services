import enum
from typing import Annotated, Any, Generic, Literal, TypeVar

from bonsai.sgen import SchemaAlias, SchemaEnum
from pydantic import AwareDatetime, Field, SerializeAsAny
from typing_extensions import TypeAliasType

from aind_behavior_services.schema_model import SchemaModel

PROTOCOL_VERSION = 0
SGEN_NAMESPACE = "AllenNeuralDynamics.AindBehaviorServices.MessageProtocol"
# From the point of view of a protocol API only the major version is relevant for de(serialization) as everything is expected to be backward compatible within the same major version.

# ================================================================================
# Core classes and types for the message protocol
# ================================================================================

TPayload = TypeVar("TPayload", bound=SchemaModel)


class MessageType(SchemaEnum, enum.StrEnum):
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


class Message(SchemaModel, Generic[TPayload]):
    """
    A generic message container that can carry any payload type.
    While not marked as abstract, it is intended to be subclassed
    for specific message types with defined payloads.

    Attributes:
        cls_type: The specific message class type identifier (discriminator)
        message_type: The category of message (request, reply, or event)
        protocol_version: The major version of the message protocol being used
        timestamp: When the message was created
        payload: The actual message content
        process_id: Identifier of the process (e.g.: executable) that created the message
        hostname: Name of the host machine that created the message
        rig_name: Name of the experimental rig that created the message
    """

    message_type: MessageType
    protocol_version: Literal[PROTOCOL_VERSION] = PROTOCOL_VERSION
    timestamp: AwareDatetime | None = Field(description="The timestamp of the message")
    payload: SerializeAsAny[TPayload] = Field(description="The payload of the message")
    process_id: str | None = Field(description="Process that created the message")
    hostname: str | None = Field(description="Hostname that created the message")
    rig_name: str | None = Field(description="Rig name that created the message")


# ================================================================================
# Core payload types
# ================================================================================
class LogLevel(SchemaEnum, enum.IntEnum):
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


class LogPayload(SchemaModel):
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

    payload_type: Literal["LogPayload"] = "LogPayload"
    message: str = Field(description="The message of the log")
    level: LogLevel = Field(default=LogLevel.DEBUG, description="The level of the log message")
    context: SerializeAsAny[Any] | None = Field(default=None, description="Additional context for the log message")
    application_version: str | None = Field(default=None, description="The version of the application")


class HeartbeatStatus(SchemaEnum, enum.IntEnum):
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


class HeartbeatPayload(SchemaModel):
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

    payload_type: Literal["HeartbeatPayload"] = "HeartbeatPayload"
    context: SerializeAsAny[Any | None] = Field(
        default=None, description="Additional context for the heartbeat message."
    )
    status: HeartbeatStatus = Field(description="The status of the heartbeat message")


# ================================================================================
# Register payloads into the protocol
# ================================================================================

RegisteredPayload = TypeAliasType(
    "RegisteredPayload",
    Annotated[LogPayload | HeartbeatPayload, Field(discriminator="payload_type"), SchemaAlias()],
)


class RegisteredMessages(Message[RegisteredPayload]):
    """A message carrying any of the registered payloads."""


class _Message(Message[Any], sgen_typename=f"{SGEN_NAMESPACE}.Message"):
    """Concrete form of `Message` for schema export, since generic models cannot be exported."""
