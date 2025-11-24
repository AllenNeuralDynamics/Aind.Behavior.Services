from enum import IntEnum
from typing import List, Literal

from pydantic import BaseModel, Field

from ._harp_gen import HarpStepperDriver


class Axis(IntEnum):
    """Motor axis available"""

    NONE = 0
    X = 1
    Y1 = 2
    Y2 = 3
    Z = 4


class ManipulatorPosition(BaseModel):
    x: float = Field(title="X coordinate")
    y1: float = Field(title="Y1 coordinate")
    y2: float = Field(title="Y2 coordinate")
    z: float = Field(title="Z coordinate")


class MicrostepResolution(IntEnum):
    MICROSTEP8 = 0
    MICROSTEP16 = 1
    MICROSTEP32 = 2
    MICROSTEP64 = 3


class MotorOperationMode(IntEnum):
    QUIET = 0
    DYNAMIC = 1


class AxisConfiguration(BaseModel):
    """Axis configuration"""

    axis: Axis = Field(title="Axis to be configured")
    step_acceleration_interval: int = Field(
        default=100,
        title="Acceleration",
        ge=2,
        le=2000,
        description="Acceleration of the step interval in microseconds",
    )
    step_interval: int = Field(
        default=100, title="Step interval", ge=100, le=20000, description="Step interval in microseconds."
    )
    microstep_resolution: MicrostepResolution = Field(
        default=MicrostepResolution.MICROSTEP8, title="Microstep resolution"
    )
    maximum_step_interval: int = Field(
        default=2000,
        ge=100,
        le=20000,
        title="Configures the time between step motor pulses (us) used when starting or stopping a movement",
    )
    motor_operation_mode: MotorOperationMode = Field(default=MotorOperationMode.QUIET, title="Motor operation mode")
    max_limit: float = Field(default=25, title="Maximum limit in SI units. A value of 0 disables this limit.")
    min_limit: float = Field(default=-0.01, title="Minimum limit in SI units. A value of 0 disables this limit.")


class AindManipulatorCalibration(BaseModel):
    description: Literal["AindManipulator calibration and settings"] = "AindManipulator calibration and settings"
    full_step_to_mm: ManipulatorPosition = Field(
        default=(ManipulatorPosition(x=0.010, y1=0.010, y2=0.010, z=0.010)),
        title="Full step to mm. Used to convert steps to SI Units",
    )
    axis_configuration: List[AxisConfiguration] = Field(
        default=[
            AxisConfiguration(axis=Axis.Y1),
            AxisConfiguration(axis=Axis.Y2),
            AxisConfiguration(axis=Axis.X),
            AxisConfiguration(axis=Axis.Z),
        ],
        title="Axes configuration. Only the axes that are configured will be enabled.",
        validate_default=True,
    )
    homing_order: List[Axis] = Field(
        default=[Axis.Y1, Axis.Y2, Axis.X, Axis.Z], title="Homing order", validate_default=True
    )
    initial_position: ManipulatorPosition = Field(
        default=ManipulatorPosition(y1=0, y2=0, x=0, z=0), validate_default=True
    )


class AindManipulator(HarpStepperDriver):
    """AindManipulator device definition"""

    calibration: AindManipulatorCalibration = Field(
        default=AindManipulatorCalibration(), description="Calibration for the device.", validate_default=True
    )
