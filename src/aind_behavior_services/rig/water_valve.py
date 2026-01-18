import logging
from typing import Annotated, Dict, List, Optional

import numpy as np
from pydantic import BaseModel, Field

from .utils import LinearRegression

logger = logging.getLogger(__name__)


PositiveFloat = Annotated[float, Field(gt=0)]


class Measurement(BaseModel):
    """Input for water valve calibration class"""

    valve_open_interval: float = Field(
        description="Time between two consecutive valve openings (s)",
        title="Valve open interval",
        gt=0,
    )
    valve_open_time: float = Field(
        description="Valve open interval (s)",
        title="Valve open time",
        gt=0,
    )
    water_weight: List[PositiveFloat] = Field(
        description="Weight of water delivered (g)",
        title="Water weight",
        min_length=1,
    )
    repeat_count: int = Field(ge=0, description="Number of times the valve opened.", title="Repeat count")


class WaterValveCalibration(BaseModel):
    """Represents a water valve calibration."""

    measurements: List[Measurement] = Field(default=[], description="List of measurements")
    interval_average: Optional[Dict[PositiveFloat, PositiveFloat]] = Field(
        default=None,
        description="Dictionary keyed by measured valve interval and corresponding average single event volume.",
        title="Interval average",
    )
    slope: float = Field(
        description="Slope of the linear regression : Volume(g) = Slope(g/s) * time(s) + offset(g)",
        title="Regression slope",
    )
    offset: float = Field(
        description="Offset of the linear regression : Volume(g) = Slope(g/s) * time(s) + offset(g)",
        title="Regression offset",
    )
    r2: Optional[float] = Field(default=None, description="R2 metric from the linear model.", title="R2", ge=0, le=1)
    valid_domain: Optional[List[PositiveFloat]] = Field(
        default=None,
        description="The optional time-intervals the calibration curve was calculated on.",
        min_length=2,
        title="Valid domain",
    )


def calibrate_water_valves(measurements: list[Measurement]) -> WaterValveCalibration:
    """Calibrate the water valve delivery system by populating the output field"""
    _x_times = []
    _y_weight = []

    for measurement in measurements:
        for weight in measurement.water_weight:
            _x_times.append(measurement.valve_open_time)
            _y_weight.append(weight / measurement.repeat_count)
    x_times = np.asarray(_x_times)
    y_weight = np.asarray(_y_weight)

    model = LinearRegression()
    model.fit(x_times.reshape(-1, 1), y_weight)
    return WaterValveCalibration(
        interval_average={x: np.mean(y_weight[x_times == x]) for x in np.unique(x_times)},
        slope=model.coef_[0],
        offset=model.intercept_,
        r2=model.score(x_times.reshape(-1, 1), y_weight),
        valid_domain=list(np.unique(x_times)),
        measurements=measurements,
    )
