import logging
from enum import Enum, IntEnum
from typing import Dict, Literal, Optional

from pydantic import BaseModel, Field

from ._harp_gen import (
    HarpOlfactometer,
)

logger = logging.getLogger(__name__)


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

    channel_index: int = Field(title="Channel index")
    channel_type: OlfactometerChannelType = Field(
        default=OlfactometerChannelType.ODOR, title="Olfactometer channel type"
    )
    flow_rate_capacity: Literal[100, 1000] = Field(default=100, title="Flow capacity. mL/min")
    flow_rate: float = Field(
        default=100, le=100, title="Target flow rate. mL/min. If channel_type == CARRIER, this value is ignored."
    )
    odorant: Optional[str] = Field(default=None, title="Odorant name")
    odorant_dilution: Optional[float] = Field(default=None, title="Odorant dilution (%v/v)")


class OlfactometerCalibration(BaseModel):
    """Olfactometer device configuration model"""

    channel_config: Dict[OlfactometerChannel, OlfactometerChannelConfig] = Field(
        default={}, description="Configuration of olfactometer channels"
    )


class Olfactometer(HarpOlfactometer):
    """A calibrated olfactometer device"""

    calibration: OlfactometerCalibration = Field(
        default=OlfactometerCalibration(), title="Calibration of the olfactometer", validate_default=True
    )
