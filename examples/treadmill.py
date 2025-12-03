from aind_behavior_services.rig import treadmill

treadmill_calibration = treadmill.TreadmillCalibration(
    wheel_diameter=10,
    pulses_per_revolution=10000,
    invert_direction=False,
    brake_lookup_calibration=[[0, 0], [0.5, 32768], [1, 65535]],
)
