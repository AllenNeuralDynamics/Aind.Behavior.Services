from typing import TYPE_CHECKING, Optional, Union

import numpy as np
from numpy.typing import NDArray

from aind_behavior_services.task.distributions import (
    BetaDistribution,
    BinomialDistribution,
    ExponentialDistribution,
    GammaDistribution,
    LogNormalDistribution,
    NormalDistribution,
    PdfDistribution,
    PoissonDistribution,
    Scalar,
    UniformDistribution,
)

if TYPE_CHECKING:
    from numpy.random import Generator

    from aind_behavior_services.task.distributions import ScalingParameters, TruncationParameters

    Distribution = Union[
        Scalar,
        NormalDistribution,
        LogNormalDistribution,
        ExponentialDistribution,
        UniformDistribution,
        PoissonDistribution,
        BinomialDistribution,
        BetaDistribution,
        GammaDistribution,
        PdfDistribution,
    ]

__all__ = ["draw_sample", "draw_samples"]

_MAX_RESAMPLE_ATTEMPTS = 1000


def _sample_raw(distribution: "Distribution", rng: "Generator", size: int = 1) -> NDArray[np.floating]:
    """Draw raw samples from the distribution without scaling or truncation."""
    params = distribution.distribution_parameters

    match distribution:
        case Scalar():
            return np.full(size, params.value)

        case NormalDistribution():
            return rng.normal(loc=params.mean, scale=params.std, size=size)

        case LogNormalDistribution():
            return rng.lognormal(mean=params.mean, sigma=params.std, size=size)

        case UniformDistribution():
            return rng.uniform(low=params.min, high=params.max, size=size)

        case ExponentialDistribution():
            if params.rate == 0:
                return np.zeros(size)
            return rng.exponential(scale=1.0 / params.rate, size=size)

        case GammaDistribution():
            if params.rate == 0:
                return np.zeros(size)
            return rng.gamma(shape=params.shape, scale=1.0 / params.rate, size=size)

        case BetaDistribution():
            return rng.beta(a=params.alpha, b=params.beta, size=size)

        case BinomialDistribution():
            return rng.binomial(n=params.n, p=params.p, size=size).astype(np.float64)

        case PoissonDistribution():
            return rng.poisson(lam=params.rate, size=size).astype(np.float64)

        case PdfDistribution():
            return rng.choice(params.index, p=params.pdf, size=size).astype(np.float64)

        case _:
            raise ValueError(f"Unsupported distribution type: {type(distribution)}")


def _apply_scaling(values: NDArray[np.floating], scaling_params: Optional["ScalingParameters"]) -> NDArray[np.floating]:
    """Apply scaling transformation: (value * scale) + offset."""
    if scaling_params is None:
        return values
    return values * scaling_params.scale + scaling_params.offset


def _apply_truncation(
    values: NDArray[np.floating], truncation_params: Optional["TruncationParameters"]
) -> NDArray[np.floating]:
    """Apply truncation to clamp values within bounds."""
    if truncation_params is None:
        return values
    if truncation_params.min == truncation_params.max:
        return values
    return np.clip(values, truncation_params.min, truncation_params.max)


def _draw_single_exclude(
    distribution: "Distribution",
    rng: "Generator",
    scaling_params: Optional["ScalingParameters"],
    min_val: float,
    max_val: float,
) -> float:
    """Draw a single sample using exclude truncation mode."""
    raw_values = _sample_raw(distribution, rng, _MAX_RESAMPLE_ATTEMPTS)
    scaled_values = _apply_scaling(raw_values, scaling_params)
    valid = scaled_values[(scaled_values >= min_val) & (scaled_values <= max_val)]

    if len(valid) > 0:
        return float(rng.choice(valid))

    # If we dont find valid samples, clamp to nearest edge
    mean_val = np.mean(scaled_values)
    if mean_val < min_val:
        return min_val
    return max_val


def draw_samples(distribution: "Distribution", n: int, rng: Optional["Generator"] = None) -> NDArray[np.floating]:
    """Draw multiple samples from a distribution with scaling and truncation applied."""
    if rng is None:
        rng = np.random.default_rng()

    truncation_params = distribution.truncation_parameters
    scaling_params = distribution.scaling_parameters
    truncation_disabled = truncation_params is None or truncation_params.min == truncation_params.max

    if truncation_disabled or truncation_params.truncation_mode == "clamp":
        raw_values = _sample_raw(distribution, rng, n)
        scaled_values = _apply_scaling(raw_values, scaling_params)
        return _apply_truncation(scaled_values, truncation_params)

    # Exclude mode: for each sample, draw 1000 values, filter, pick one
    assert truncation_params is not None
    min_val, max_val = truncation_params.min, truncation_params.max
    return np.array([_draw_single_exclude(distribution, rng, scaling_params, min_val, max_val) for _ in range(n)])


def draw_sample(distribution: "Distribution", rng: Optional["Generator"] = None) -> float:
    """Draw a single sample from a distribution with scaling and truncation applied."""
    return float(draw_samples(distribution, 1, rng)[0])
