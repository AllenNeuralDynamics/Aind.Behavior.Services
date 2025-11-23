import os
from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field, SerializeAsAny, model_validator

from aind_behavior_services.base import SchemaVersionedModel


class Device(BaseModel):
    """A device in the rig configuration.
    All devices are expected to derive from this base class.
    """

    device_type: str = Field(description="Device type")
    name: str = Field(description="Device name")
    settings: Optional[SerializeAsAny[BaseModel]] = Field(default=None, description="Device settings")
    additional_settings: Optional[SerializeAsAny[BaseModel]] = Field(
        default=None, description="Additional settings", deprecated="Use *settings* field instead."
    )
    calibration: Optional[SerializeAsAny[BaseModel]] = Field(
        default=None, description="Calibration", deprecated="Use *settings* field instead."
    )

    @model_validator(mode="after")
    def ensure_settings_synched(self):
        if "additional_settings" or "calibration" in self.model_fields_set:
            raise ValueError(
                "The fields 'additional_settings' and 'calibration' are deprecated. Please use the 'settings' field instead."
            )
        self.additional_settings = self.calibration = self.settings


class AindBehaviorRigModel(SchemaVersionedModel):
    """Base model for rig configuration. All rig configurations should derive from this base class."""

    computer_name: str = Field(default_factory=lambda: os.environ["COMPUTERNAME"], description="Computer name")
    rig_name: str = Field(description="Rig name")
    data_directory: Path = Field(description="Directory where data will be saved to")
