import logging
from typing import Annotated, List

from pydantic import BaseModel, Field, field_validator

from ._harp_gen import HarpLoadCells

logger = logging.getLogger(__name__)

LoadCellChannel = Annotated[int, Field(ge=0, le=7, description="Load cell channel number available")]

LoadCellOffset = Annotated[int, Field(ge=-255, le=255, description="Load cell offset value [-255, 255]")]


class LoadCellChannelCalibration(BaseModel):
    """Load cell channel calibration
    Calibration will be applied as:
        weight (g) = slope * (adc_units_corrected_by_offset_resistor - adc_units_baseline)
    """

    channel: LoadCellChannel
    offset: LoadCellOffset = Field(default=0, title="Load cell offset applied to the wheatstone bridge circuit")
    baseline: float = Field(default=0.0, title="Load cell baseline that will be DSP subtracted to the raw adc output.")
    slope: float = Field(
        default=1.0, title="Load cell slope that will be used to convert tared (- baseline) adc units to weight (g)."
    )


class LoadCellsCalibration(BaseModel):
    """Load cells calibration"""

    channels: List["LoadCellChannelCalibration"] = Field(
        default=[], title="Load cells calibration", validate_default=True
    )

    @field_validator("channels", mode="after")
    @classmethod
    def ensure_unique_channels(cls, values: List["LoadCellChannelCalibration"]) -> List["LoadCellChannelCalibration"]:
        channels = [c.channel for c in values]
        if len(channels) != len(set(channels)):
            raise ValueError("Channels must be unique.")
        return values


class LoadCells(HarpLoadCells):
    """Load cells device"""

    calibration: LoadCellsCalibration = Field(
        default=LoadCellsCalibration(), description="Calibration for the device.", validate_default=True
    )
