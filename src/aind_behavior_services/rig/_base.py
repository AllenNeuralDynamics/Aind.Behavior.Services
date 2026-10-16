from pathlib import Path

from bonsai.sgen import SchemaModel
from pydantic import Field

from aind_behavior_services.base import DefaultAwareDatetime, SchemaVersionedModel

SGEN_NAMESPACE = "AllenNeuralDynamics.AindBehaviorServices.Rig"


class Device(SchemaModel):
    """A device in the rig configuration.
    All devices are expected to derive from this base class.
    """

    device_type: str = Field(description="Device type")
    # TODO: restore `calibration: SerializeAsAny[BaseModel] | None` once bonsai-sgen can export subclasses of a base with a SerializeAsAny field.


class DatedCalibration(SchemaModel):
    """Base model for dated calibrations."""

    date: DefaultAwareDatetime | None = Field(default=None, description="Date of the calibration")


class Rig(SchemaVersionedModel):
    """Base model for rig configuration. All rig configurations should derive from this base class."""

    computer_name: str = Field(description="Computer name")
    rig_name: str = Field(description="Rig name")
    data_directory: Path = Field(description="Directory where data will be saved to")
