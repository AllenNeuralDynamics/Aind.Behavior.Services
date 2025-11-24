from aind_behavior_services.rig import water_valve as wv


def linear_model(time, slope, offset):
    return slope * time + offset


_delta_times = [0.1, 0.2, 0.3, 0.4, 0.5]
_slope = 10.1
_offset = -0.3

_water_weights = [linear_model(x, _slope, _offset) for x in _delta_times]
_inputs = [
    wv.Measurement(valve_open_interval=0.5, valve_open_time=t[0], water_weight=[t[1]], repeat_count=1)
    for t in zip(_delta_times, _water_weights)
]

calibration = wv.calibrate_water_valves(_inputs)
