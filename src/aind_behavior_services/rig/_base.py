import os
from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field, SerializeAsAny

from aind_behavior_services.base import SchemaVersionedModel


class Device(BaseModel):
    """A device in the rig configuration.
    All devices are expected to derive from this base class.
    """

    device_type: str = Field(description="Device type")
    calibration: Optional[SerializeAsAny[BaseModel]] = Field(default=None, description="Calibration for the device.")


class AindBehaviorRigModel(SchemaVersionedModel):
    """Base model for rig configuration. All rig configurations should derive from this base class."""

    computer_name: str = Field(default_factory=lambda: os.environ["COMPUTERNAME"], description="Computer name")
    rig_name: str = Field(description="Rig name")
    data_directory: Path = Field(description="Directory where data will be saved to")
