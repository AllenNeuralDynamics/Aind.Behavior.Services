from pydantic import BaseModel, Field


class ZmqConnection(BaseModel):
    connection_string: str = Field(
        default="@tcp://localhost:5556", description="The connection string for the ZMQ socket."
    )
    topic: str = Field(default="")
