from typing import Literal, Optional

from pydantic import BaseModel, Field, model_validator


class ZmqConnection(BaseModel):
    protocol: Literal["Tcp"] = Field(default="Tcp", description="The protocol to use for the ZMQ connection.")
    address: str = Field(default="localhost", description="The address of the ZMQ socket.")
    port: int = Field(default=5556, description="The port of the ZMQ socket.")
    action: Optional[Literal["bind", "connect"]] = Field(
        default=None, description="Whether to bind or connect the socket."
    )
    connection_string: str = Field(default="", description="The connection string for the ZMQ socket.")
    topic: str = Field(default="")

    @model_validator(mode="after")
    def set_connection_string(self) -> "ZmqConnection":
        if not self.connection_string:
            self.connection_string = (
                f"{_action_character_map[self.action]}{self.protocol.lower()}://{self.address}:{self.port}"
            )
        return self


_action_character_map: dict[str | None, str] = {
    "bind": ">",
    "connect": "@",
    None: "",
}
