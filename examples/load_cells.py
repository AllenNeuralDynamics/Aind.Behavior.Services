from aind_behavior_services.rig import load_cells as lc

lc0 = lc.LoadCellChannelCalibration(
    channel=0,
    baseline=0.1,
    offset=100,
    slope=2.0,
)

lc1 = lc.LoadCellChannelCalibration(
    channel=1,
    baseline=0.2,
    offset=150,
    slope=1.5,
)

lc_calibration_input = lc.LoadCellsCalibration(channels=[lc1, lc0])
