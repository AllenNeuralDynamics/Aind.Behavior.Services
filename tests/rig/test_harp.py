import unittest
from typing import List, Literal, Optional

from pydantic import Field

from aind_behavior_services.rig import (
    Rig,
)
from aind_behavior_services.rig.harp import (
    ConnectedClockOutput,
    HarpDevice,
    HarpDeviceGeneric,
    HarpWhiteRabbit,
    validate_harp_clock_output,
)


class TestHarpClockOutput(unittest.TestCase):
    class ZeroHarpDevice(Rig):
        data_directory: str = "/data"
        rig_name: str = "rig"
        computer_name: str = "computer"
        version: Literal["0.0.0"] = "0.0.0"

    class OneHarpDevice(Rig):
        data_directory: str = "/data"
        rig_name: str = "rig"
        computer_name: str = "computer"
        version: Literal["0.0.0"] = "0.0.0"
        harp_device: Optional[HarpDevice]

    class NHarpDevice(Rig):
        data_directory: str = "/data"
        rig_name: str = "rig"
        computer_name: str = "computer"
        version: Literal["0.0.0"] = "0.0.0"
        harp_device: Optional[HarpDevice] = None
        harp_white_rabbit: Optional[HarpWhiteRabbit] = None
        harp_device_array: List[HarpDevice] = Field(default_factory=list)

    def setUp(self):
        self.generic_harp = HarpDeviceGeneric(port_name="COM1", name="GenericHarp")
        self.write_rabbit = HarpWhiteRabbit(port_name="COM2", name="WhiteRabbit")

    @staticmethod
    def _add_clk_out(white_rabbit: HarpWhiteRabbit, n: int) -> HarpWhiteRabbit:
        white_rabbit.connected_clock_outputs = [ConnectedClockOutput(output_channel=i) for i in range(n)]
        return white_rabbit

    def test_zero_harp(self):
        validate_harp_clock_output(self.ZeroHarpDevice())

    def test_one_harp(self):
        validate_harp_clock_output(self.OneHarpDevice(harp_device=self.generic_harp))
        validate_harp_clock_output(self.OneHarpDevice(harp_device=None))

    def test_multiple_devices_no_synchronizer(self):
        validate_harp_clock_output(self.NHarpDevice(harp_device=self.generic_harp))
        validate_harp_clock_output(self.NHarpDevice(harp_device=None))
        validate_harp_clock_output(self.NHarpDevice(harp_device_array=[self.generic_harp]))
        validate_harp_clock_output(self.NHarpDevice(harp_device=None, harp_device_array=[self.generic_harp]))
        validate_harp_clock_output(
            self.NHarpDevice(
                harp_device=None, harp_white_rabbit=self._add_clk_out(self.write_rabbit, 0), harp_device_array=[]
            )
        )

    def test_multiple_devices_with_synchronizer(self):
        validate_harp_clock_output(
            self.NHarpDevice(
                harp_device=self.generic_harp,
                harp_white_rabbit=self._add_clk_out(self.write_rabbit, 3),
                harp_device_array=[self.generic_harp, self.generic_harp],
            )
        )

        with self.assertRaises(ValueError) as _:
            validate_harp_clock_output(
                self.NHarpDevice(
                    harp_device=self.generic_harp,
                    harp_white_rabbit=self._add_clk_out(self.write_rabbit, 4),
                    harp_device_array=[self.generic_harp, self.generic_harp],
                )
            )

        validate_harp_clock_output(
            self.NHarpDevice(
                harp_device=None,
                harp_white_rabbit=self._add_clk_out(self.write_rabbit, 2),
                harp_device_array=[self.generic_harp, self.generic_harp],
            )
        )

        with self.assertRaises(ValueError) as _:
            validate_harp_clock_output(
                self.NHarpDevice(
                    harp_device=None,
                    harp_white_rabbit=self._add_clk_out(self.write_rabbit, 1),
                    harp_device_array=[self.generic_harp, self.generic_harp],
                )
            )

        validate_harp_clock_output(
            self.NHarpDevice(
                harp_device=self.generic_harp,
                harp_white_rabbit=self._add_clk_out(self.write_rabbit, 3),
                harp_device_array=[self.generic_harp, self.generic_harp],
            )
        )

        validate_harp_clock_output(
            self.NHarpDevice(
                harp_device=None, harp_white_rabbit=self._add_clk_out(self.write_rabbit, 2), harp_device_array=[]
            )
        )

        with self.assertRaises(ValueError) as _:
            validate_harp_clock_output(
                self.NHarpDevice(harp_device=self.generic_harp, harp_device_array=[self.generic_harp])
            )
        with self.assertRaises(ValueError) as _:
            validate_harp_clock_output(
                self.NHarpDevice(harp_device=None, harp_device_array=[self.generic_harp, self.generic_harp])
            )


if __name__ == "__main__":
    unittest.main()
