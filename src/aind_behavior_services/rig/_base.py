from pathlib import Path
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field, SerializeAsAny, model_validator

from aind_behavior_services.base import DefaultAwareDatetime, SchemaVersionedModel
from aind_behavior_services.utils import utcnow


class Device(BaseModel):
    """A device in the rig configuration.
    All devices are expected to derive from this base class.
    """

    device_type: str = Field(description="Device type")
    calibration: Optional[SerializeAsAny[BaseModel]] = Field(default=None, description="Calibration for the device.")


class DatedCalibration(BaseModel):
    """Base model for dated calibrations."""

    date: DefaultAwareDatetime = Field(description="Date of the calibration")

    @model_validator(mode="before")
    @classmethod
    def _default_date_now(cls, values: Any) -> Any:
        """If no date is provided, use the current date and time."""
        if isinstance(values, Dict) and "date" not in values:
            values["date"] = utcnow()
        return values


class Rig(SchemaVersionedModel):
    """Base model for rig configuration. All rig configurations should derive from this base class."""

    computer_name: str = Field(description="Computer name")
    rig_name: str = Field(description="Rig name")
    data_directory: Path = Field(description="Directory where data will be saved to")
