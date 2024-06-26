from __future__ import annotations

import os
from enum import Enum
from typing import Annotated, Dict, Generic, Literal, Optional, TypeVar, Union

from aind_behavior_services.base import SchemaVersionedModel, coerce_schema_version
from pydantic import BaseModel, Field, RootModel, field_validator


class Device(BaseModel):
    device_type: str = Field(..., description="Device type")
    additional_settings: Optional[BaseModel] = Field(default=None, description="Additional settings")
    calibration: Optional[BaseModel] = Field(default=None, description="Calibration")


class VideoWriterFfmpeg(BaseModel):
    video_writer_type: Literal["FFMPEG"] = Field(default="FFMPEG")
    frame_rate: int = Field(default=30, ge=0, description="Encoding frame rate")
    container_extension: str = Field(default="mp4", description="Container extension")
    output_arguments: str = Field(
        default="-c:v hevc_nvenc -pix_fmt x2rgb10le -color_range full -tune hq -preset p3 -rc vbr -cq 16 -rc-lookahead 56 -temporal-aq 1 -qmin 0 -qmax 10",  # noqa E501
        description="Output arguments",
    )


class VideoWriterOpenCv(BaseModel):
    video_writer_type: Literal["OPENCV"] = Field(default="OPENCV")
    frame_rate: int = Field(default=30, ge=0, description="Encoding frame rate")
    container_extension: str = Field(default="avi", description="Container extension")
    four_cc: str = Field(default="FMP4", description="Four character code")


class VideoWriter(RootModel):
    root: Annotated[Union[VideoWriterFfmpeg, VideoWriterOpenCv], Field(discriminator="video_writer_type")]


class WebCamera(Device):
    device_type: Literal["WebCamera"] = Field(default="WebCamera", description="Device type")
    index: int = Field(default=0, ge=0, description="Camera index")
    video_writer: Optional[VideoWriter] = Field(
        default=None, description="Video writer. If not provided, no video will be saved."
    )


class SpinnakerCamera(Device):
    device_type: Literal["SpinnakerCamera"] = Field(default="SpinnakerCamera", description="Device type")
    serial_number: str = Field(..., description="Camera serial number")
    binning: int = Field(default=1, ge=1, description="Binning")
    color_processing: Literal["Default", "NoColorProcessing"] = Field(default="Default", description="Color processing")
    exposure: int = Field(default=1000, ge=100, description="Exposure time")
    gain: float = Field(default=0, ge=0, description="Gain")
    video_writer: Optional[VideoWriter] = Field(
        default=None, description="Video writer. If not provided, no video will be saved."
    )


TCamera = TypeVar("TCamera", bound=Union[WebCamera, SpinnakerCamera])


class CameraController(Device, Generic[TCamera]):
    device_type: Literal["CameraController"] = "CameraController"
    cameras: Dict[str, TCamera] = Field(..., description="Cameras to be instantiated")
    frame_rate: Optional[int] = Field(default=30, ge=0, description="Frame rate of the trigger to all cameras")


class HarpDeviceType(str, Enum):
    LOADCELLS = "loadcells"
    BEHAVIOR = "behavior"
    OLFACTOMETER = "olfactometer"
    CLOCKGENERATOR = "clockgenerator"
    CLOCKSYNCHRONIZER = "clocksynchronizer"
    TREADMILL = "treadmill"
    LICKOMETER = "lickometer"
    ANALOGINPUT = "analoginput"
    SOUNDCARD = "soundcard"
    SNIFFDETECTOR = "sniffdetector"
    CUTTLEFISH = "cuttlefish"
    STEPPERDRIVER = "stepperdriver"
    GENERIC = "generic"


class HarpDeviceGeneric(Device):
    who_am_i: Optional[int] = Field(default=None, le=9999, ge=0, description="Device WhoAmI")
    device_type: Literal[HarpDeviceType.GENERIC] = HarpDeviceType.GENERIC
    serial_number: Optional[str] = Field(default=None, description="Device serial number")
    port_name: str = Field(..., description="Device port name")


class HarpBehavior(HarpDeviceGeneric):
    device_type: Literal[HarpDeviceType.BEHAVIOR] = HarpDeviceType.BEHAVIOR
    who_am_i: Literal[1216] = 1216


class HarpSoundCard(HarpDeviceGeneric):
    device_type: Literal[HarpDeviceType.SOUNDCARD] = HarpDeviceType.SOUNDCARD
    who_am_i: Literal[1280] = 1280


class HarpLoadCells(HarpDeviceGeneric):
    device_type: Literal[HarpDeviceType.LOADCELLS] = HarpDeviceType.LOADCELLS
    who_am_i: Literal[1232] = 1232


class HarpOlfactometer(HarpDeviceGeneric):
    device_type: Literal[HarpDeviceType.OLFACTOMETER] = HarpDeviceType.OLFACTOMETER
    who_am_i: Literal[1140] = 1140


class HarpClockGenerator(HarpDeviceGeneric):
    device_type: Literal[HarpDeviceType.CLOCKGENERATOR] = HarpDeviceType.CLOCKGENERATOR
    who_am_i: Literal[1158] = 1158


class HarpClockSynchronizer(HarpDeviceGeneric):
    device_type: Literal[HarpDeviceType.CLOCKSYNCHRONIZER] = HarpDeviceType.CLOCKSYNCHRONIZER
    who_am_i: Literal[1152] = 1152


class HarpAnalogInput(HarpDeviceGeneric):
    device_type: Literal[HarpDeviceType.ANALOGINPUT] = HarpDeviceType.ANALOGINPUT
    who_am_i: Literal[1236] = 1236


class HarpLickometer(HarpDeviceGeneric):
    device_type: Literal[HarpDeviceType.LICKOMETER] = HarpDeviceType.LICKOMETER
    who_am_i: Literal[1400] = 1400


class HarpSniffDetector(HarpDeviceGeneric):
    device_type: Literal[HarpDeviceType.SNIFFDETECTOR] = HarpDeviceType.SNIFFDETECTOR
    who_am_i: Literal[1401] = 1401


class HarpTreadmill(HarpDeviceGeneric):
    device_type: Literal[HarpDeviceType.TREADMILL] = HarpDeviceType.TREADMILL
    who_am_i: Literal[1402] = 1402


class HarpCuttlefish(HarpDeviceGeneric):
    device_type: Literal[HarpDeviceType.CUTTLEFISH] = HarpDeviceType.CUTTLEFISH
    who_am_i: Literal[1403] = 1403


class HarpStepperDriver(HarpDeviceGeneric):
    device_type: Literal[HarpDeviceType.STEPPERDRIVER] = HarpDeviceType.STEPPERDRIVER
    who_am_i: Literal[1130] = 1130


class HarpDevice(RootModel):
    root: Annotated[
        Union[
            HarpBehavior,
            HarpOlfactometer,
            HarpClockGenerator,
            HarpAnalogInput,
            HarpLickometer,
            HarpTreadmill,
            HarpCuttlefish,
            HarpLoadCells,
            HarpSoundCard,
            HarpSniffDetector,
            HarpClockSynchronizer,
            HarpStepperDriver,
        ],
        Field(discriminator="device_type"),
    ]


class Screen(Device):
    device_type: Literal["Screen"] = Field(default="Screen", description="Device type")
    display_index: int = Field(default=1, description="Display index")
    target_render_frequency: float = Field(default=60, description="Target render frequency")
    target_update_frequency: float = Field(default=120, description="Target update frequency")
    calibration_directory: str = Field(default="Calibration\\Monitors\\", description="Calibration directory")
    texture_assets_directory: str = Field(default="Textures", description="Calibration directory")
    brightness: float = Field(default=0, le=1, ge=-1, description="Brightness")
    contrast: float = Field(default=1, le=1, ge=-1, description="Contrast")


class Treadmill(BaseModel):
    wheel_diameter: float = Field(default=15, ge=0, description="Wheel diameter")
    pulses_per_revolution: int = Field(default=28800, ge=1, description="Pulses per revolution")
    invert_direction: bool = Field(default=False, description="Invert direction")


class AindBehaviorRigModel(SchemaVersionedModel):
    computer_name: str = Field(default_factory=lambda: os.environ["COMPUTERNAME"], description="Computer name")
    rig_name: str = Field(..., description="Rig name")

    @field_validator("version", mode="before")
    @classmethod
    def coerce_version(cls, v: str) -> str:
        return coerce_schema_version(cls, v)
