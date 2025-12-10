import logging
from typing import ClassVar, List

from pydantic import BaseModel, Field, field_validator

from aind_behavior_services.patterns import ValuePair

from ._harp_gen import HarpTreadmill

logger = logging.getLogger(__name__)


class TreadmillCalibration(BaseModel):
    """Treadmill calibration class"""

    _BRAKE_OUTPUT_MAX: ClassVar[float] = 65535
    _BRAKE_OUTPUT_MIN: ClassVar[float] = 0
    _BRAKE_INPUT_MAX: ClassVar[float] = float("inf")
    _BRAKE_INPUT_MIN: ClassVar[float] = 0

    wheel_diameter: float = Field(default=15, ge=0, description="Wheel diameter")
    pulses_per_revolution: int = Field(default=28800, ge=1, description="Pulses per revolution")
    invert_direction: bool = Field(default=False, description="Invert direction")
    brake_lookup_calibration: List[ValuePair] = Field(
        default=[[0, 0], [1, 65535]],
        validate_default=True,
        min_length=2,
        description="Brake lookup calibration. Each pair of values define (input [torque], output [brake set-point U16])",
    )

    @field_validator("brake_lookup_calibration", mode="after")
    @classmethod
    def validate_brake_lookup_calibration(cls, value: List[ValuePair]) -> List[ValuePair]:
        for pair in value:
            if pair[0] < cls._BRAKE_INPUT_MIN or pair[0] > cls._BRAKE_INPUT_MAX:
                raise ValueError(f"Brake input value must be between {cls._BRAKE_INPUT_MIN} and {cls._BRAKE_INPUT_MAX}")
            if pair[1] < cls._BRAKE_OUTPUT_MIN or pair[1] > cls._BRAKE_OUTPUT_MAX:
                raise ValueError(
                    f"Brake output value must be between {cls._BRAKE_OUTPUT_MIN} and {cls._BRAKE_OUTPUT_MAX}"
                )
        return value


class Treadmill(HarpTreadmill):
    """A calibrated treadmill device"""

    calibration: TreadmillCalibration = Field(
        default=TreadmillCalibration(), title="Calibration of the treadmill", validate_default=True
    )
