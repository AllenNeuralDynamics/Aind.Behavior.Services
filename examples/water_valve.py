from datetime import datetime

from aind_behavior_services.calibration.water_valve import (
    Measurement,
    WaterValveCalibration,
    WaterValveCalibrationInput,
    WaterValveCalibrationOutput,
)

_delta_times = [0.1, 0.2, 0.3, 0.4, 0.5]
_slope = 10.1
_offset = -0.3
_linear_model = lambda time: _slope * time + _offset
_water_weights = [_linear_model(x) for x in _delta_times]
_inputs = [
    Measurement(valve_open_interval=0.5, valve_open_time=t[0], water_weight=[t[1]], repeat_count=1)
    for t in zip(_delta_times, _water_weights)
]


_outputs = WaterValveCalibrationOutput(
    interval_average={interval: volume for interval, volume in zip(_delta_times, _water_weights)},
    slope=_slope,
    offset=_offset,
    r2=1.0,
    valid_domain=[value for value in _delta_times],
)

input = WaterValveCalibrationInput(measurements=_inputs)
calibration = WaterValveCalibration(
    input=input,
    output=input.calibrate_output(),
    device_name="WaterValve",
    calibration_date=datetime.now(),
)
