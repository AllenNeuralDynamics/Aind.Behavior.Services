import unittest

from pydantic import ValidationError

from aind_behavior_services.rig.water_valve import Measurement, WaterValveCalibration, calibrate_water_valves


class WaterValveTests(unittest.TestCase):
    """Tests the water calibration model."""

    def test_calibration(self):
        """Test the compare_version method."""

        _delta_times = [0.1, 0.2, 0.3, 0.4, 0.5]
        _slope = 10.1
        _offset = -0.3
        _water_weights = [water_mock_model(x, _slope, _offset) for x in _delta_times]
        _inputs = [
            Measurement(valve_open_interval=0.5, valve_open_time=t[0], water_weight=[t[1]], repeat_count=1)
            for t in zip(_delta_times, _water_weights)
        ]

        calibration = calibrate_water_valves(measurements=_inputs)

        try:
            WaterValveCalibration.model_validate_json(calibration.model_dump_json())
        except ValidationError as e:
            self.fail(f"Validation failed with error: {e}")

    def test_calibration_on_null_output(self):
        """Test the compare_version method."""

        _delta_times = [0.1, 0.2, 0.3, 0.4, 0.5]
        _slope = 10.1
        _offset = -0.3
        _water_weights = [water_mock_model(x, _slope, _offset) for x in _delta_times]
        calibration = calibrate_water_valves(
            measurements=[
                Measurement(valve_open_interval=0.5, valve_open_time=t[0], water_weight=[t[1]], repeat_count=1)
                for t in zip(_delta_times, _water_weights)
            ]
        )

        self.assertAlmostEqual(_slope, calibration.slope, 2, "Slope is not almost equal")
        self.assertAlmostEqual(_offset, calibration.offset, 2, "Offset is not almost equal")
        self.assertIsNotNone(calibration.r2, "R2 is None")
        self.assertAlmostEqual(1.0, calibration.r2, 2, "R2 is not almost equal")


def water_mock_model(time: float, slope: float, offset: float) -> float:
    return slope * time + offset


if __name__ == "__main__":
    unittest.main()
