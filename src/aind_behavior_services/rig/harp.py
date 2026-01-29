from typing import TypeAlias, TypeVar

from ..rig._base import Rig
from ..utils import get_fields_of_type
from ._harp_gen import *  # noqa # We re-export all auto-generated Harp devices here
from ._harp_gen import ConnectedClockOutput, _HarpDeviceBase

HarpDeviceBase: TypeAlias = _HarpDeviceBase

TRig = TypeVar("TRig", bound=Rig)


def validate_harp_clock_output(rig: TRig) -> TRig:
    """Validates that the number of Harp devices in the rig configuration matches the number of connected clock outputs."""
    harp_devices = get_fields_of_type(rig, _HarpDeviceBase)
    if len(harp_devices) < 2:
        return rig
    n_clock_targets = len(harp_devices) - 1
    clock_outputs = get_fields_of_type(rig, ConnectedClockOutput)
    if len(clock_outputs) != n_clock_targets:
        raise ValueError(f"Expected {n_clock_targets} clock outputs, got {len(clock_outputs)}")
    return rig
