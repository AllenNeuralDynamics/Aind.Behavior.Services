from enum import Enum, IntEnum
from typing import Any, Dict, Literal, Mapping, Optional

from pydantic import BaseModel, Field, model_validator

from ._base import DatedCalibration
from ._harp_gen import (
    HarpOlfactometer,
)


class OlfactometerChannel(IntEnum):
    """Harp Olfactometer available channel"""

    Channel0 = 0
    Channel1 = 1
    Channel2 = 2
    Channel3 = 3


class OlfactometerChannelType(str, Enum):
    """Olfactometer channel type"""

    ODOR = "Odor"
    CARRIER = "Carrier"


class OlfactometerChannelConfig(BaseModel):
    """Configuration for a single olfactometer channel"""

    channel_type: OlfactometerChannelType = Field(
        default=OlfactometerChannelType.ODOR, title="Olfactometer channel type"
    )
    flow_rate_capacity: Literal[100, 1000] = Field(default=100, title="Flow capacity. mL/min")
    odorant: Optional[str] = Field(default=None, title="Odorant name")
    odorant_dilution: Optional[float] = Field(default=None, title="Odorant dilution (%v/v)")


class OlfactometerCalibration(DatedCalibration):
    """Olfactometer device configuration model"""

    channel0: Optional[OlfactometerChannelConfig] = Field(default=None, title="Configuration for channel 0")
    channel1: Optional[OlfactometerChannelConfig] = Field(default=None, title="Configuration for channel 1")
    channel2: Optional[OlfactometerChannelConfig] = Field(default=None, title="Configuration for channel 2")
    channel3: Optional[OlfactometerChannelConfig] = Field(default=None, title="Configuration for channel 3")

    @model_validator(mode="before")
    @classmethod
    def _deserialize_legacy_channel_config(cls, data: Any) -> Any:
        """Back-compat: accept deprecated `channel_config` on input only."""
        if not isinstance(data, Mapping):
            return data

        parsed = dict(data)
        legacy = parsed.pop("channel_config", None)  # remove so it is never serialized back
        if not isinstance(legacy, Mapping):
            return parsed

        valid_indices = {channel.value for channel in OlfactometerChannel}

        for raw_key, config in legacy.items():
            idx: Optional[int] = None

            # Legacy payload keys are expected to be "0", "1", "2", "3"
            if isinstance(raw_key, int):
                idx = raw_key
            elif isinstance(raw_key, str):
                key = raw_key.strip().lower()
                if key.isdigit():
                    idx = int(key)
                elif key.startswith("channel") and key[7:].isdigit():
                    idx = int(key[7:])

            if idx in valid_indices:
                parsed.setdefault(f"channel{idx}", config)

        return parsed

    def as_dictionary(self) -> Dict[OlfactometerChannel, OlfactometerChannelConfig]:
        """Return the channel configuration as a dictionary"""
        return {
            channel: config
            for channel in OlfactometerChannel
            if (config := getattr(self, f"channel{channel.value}")) is not None
        }


class StrictOlfactometerCalibration(OlfactometerCalibration):
    """Strict olfactometer calibration where all channels must be defined"""

    channel0: OlfactometerChannelConfig = Field(title="Configuration for channel 0")
    channel1: OlfactometerChannelConfig = Field(title="Configuration for channel 1")
    channel2: OlfactometerChannelConfig = Field(title="Configuration for channel 2")
    channel3: OlfactometerChannelConfig = Field(title="Configuration for channel 3")


class StrictOlfactometer(HarpOlfactometer):
    """A calibrated olfactometer device where all channels must be defined"""

    calibration: StrictOlfactometerCalibration = Field(title="Calibration of the olfactometer", validate_default=True)


class Olfactometer(HarpOlfactometer):
    """A calibrated olfactometer device"""

    calibration: OlfactometerCalibration = Field(
        default=OlfactometerCalibration(), title="Calibration of the olfactometer", validate_default=True
    )
