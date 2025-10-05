import os
from typing import Optional, Self, TypeVar

from pydantic import BaseModel, Field, model_validator

from aind_behavior_services.base import SchemaVersionedModel


class Device(BaseModel):
    device_type: str = Field(..., description="Device type")
    name: Optional[str] = Field(default=None, description="Device name", alias="device_name")
    additional_settings: Optional[BaseModel] = Field(default=None, description="Additional settings")
    calibration: Optional[BaseModel] = Field(default=None, description="Calibration")

    # For backward compatibility, we need to set the device name to the device type if it is not provided.
    # We should consider removing this in the future.
    @model_validator(mode="after")
    def _set_name(self) -> Self:
        if (name := self.name) is None:
            if self.calibration is not None:
                name = getattr(self.calibration, "device_name", None)
            if name is None:
                name = self.device_type
            self.name = name
        return self


class AindBehaviorRigModel(SchemaVersionedModel):
    computer_name: str = Field(default_factory=lambda: os.environ["COMPUTERNAME"], description="Computer name")
    rig_name: str = Field(..., description="Rig name")


def _default_rig_name() -> str:
    if "RIG_NAME" not in os.environ:
        raise ValueError("RIG_NAME environment variable is not set. An explicit rig name must be provided.")
    else:
        return os.environ["RIG_NAME"]


TRig = TypeVar("TRig", bound=AindBehaviorRigModel)
