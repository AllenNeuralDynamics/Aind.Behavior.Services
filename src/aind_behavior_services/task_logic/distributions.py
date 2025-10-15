from enum import Enum
from typing import Annotated, Any, List, Literal, Optional, Self, Union

from pydantic import BaseModel, BeforeValidator, Field, NonNegativeFloat, field_validator, model_validator
from typing_extensions import TypeAliasType


class TruncationParameters(BaseModel):
    """
    Parameters for truncating a distribution to a specified range. Truncation should
    be applied after sampling and scaling.

    The truncation_mode determines how out-of-bounds values are handled:
    - "exclude": Resample until a value within [min, max] is obtained.
    If after a certain number of attempts no valid value is found, it
    will use the average of sampled values and pick the closest bound.
    - "clamp": Clamp values to the nearest bound within [min, max].
    Used to constrain sampled values within minimum and maximum bounds.
    """

    truncation_mode: Literal["exclude", "clamp"] = Field(default="exclude", description="Mode of truncation to apply")
    min: float = Field(default=0, description="Minimum value of the sampled distribution")
    max: float = Field(default=0, description="Maximum value of the sampled distribution")

    @model_validator(mode="after")
    def validate_min_less_than_max(self) -> Self:
        """Ensures that min is less than max when truncation is enabled"""
        if self.min > self.max:
            raise ValueError("Truncation min must be less than truncation max")
        return self


class ScalingParameters(BaseModel):
    """
    Parameters for scaling and offsetting sampled distribution values.
    Scaling is applied as (value * scale + offset).

    Applies linear transformation: result = (value * scale) + offset.
    """

    scale: float = Field(default=1, description="Scaling factor to apply on the sampled distribution")
    offset: float = Field(default=0, description="Offset factor to apply on the sampled distribution")


class DistributionFamily(str, Enum):
    """
    Enumeration of supported probability distribution families.

    Defines all available statistical distributions that can be used
    for sampling random values in the task logic system.
    """

    SCALAR = "Scalar"
    NORMAL = "Normal"
    LOGNORMAL = "LogNormal"
    UNIFORM = "Uniform"
    EXPONENTIAL = "Exponential"
    GAMMA = "Gamma"
    BINOMIAL = "Binomial"
    BETA = "Beta"
    POISSON = "Poisson"
    PDF = "Pdf"


class DistributionParametersBase(BaseModel):
    """
    Base class for all distribution parameter models. This class should not be instantiated directly.

    Provides common family field for discriminated union validation.
    """

    family: DistributionFamily = Field(..., description="Family of the distribution")


class DistributionBase(BaseModel):
    """
    Base class for all distribution models. This class should not be instantiated directly.

    Combines distribution parameters with optional truncation and scaling
    transformations for flexible probability distributions.
    """

    family: DistributionFamily = Field(..., description="Family of the distribution")
    distribution_parameters: "DistributionParameters" = Field(..., description="Parameters of the distribution")
    truncation_parameters: Optional[TruncationParameters] = Field(
        default=None, description="Truncation parameters of the distribution"
    )
    scaling_parameters: Optional[ScalingParameters] = Field(
        default=None, description="Scaling parameters of the distribution"
    )


class ScalarDistributionParameter(DistributionParametersBase):
    """
    Parameters for a scalar (constant) distribution.

    Represents a deterministic value that always returns the same number.
    """

    family: Literal[DistributionFamily.SCALAR] = DistributionFamily.SCALAR
    value: float = Field(default=0, description="The static value of the distribution")


class Scalar(DistributionBase):
    """
    A scalar distribution that returns a constant value.

    Useful for fixed parameters that don't vary across trials or samples.
    """

    family: Literal[DistributionFamily.SCALAR] = DistributionFamily.SCALAR
    distribution_parameters: ScalarDistributionParameter = Field(
        default=ScalarDistributionParameter(), description="Parameters of the distribution"
    )
    truncation_parameters: Literal[None] = None
    scaling_parameters: Literal[None] = None


class NormalDistributionParameters(DistributionParametersBase):
    """
    Parameters for a normal (Gaussian) distribution.

    Defined by mean (center) and standard deviation (spread).
    """

    family: Literal[DistributionFamily.NORMAL] = DistributionFamily.NORMAL
    mean: float = Field(default=0, description="Mean of the distribution")
    std: float = Field(default=0, description="Standard deviation of the distribution")


class NormalDistribution(DistributionBase):
    """
    A normal (Gaussian) probability distribution.

    Bell-shaped distribution symmetric around the mean, commonly used
    for modeling naturally occurring random variables.
    """

    family: Literal[DistributionFamily.NORMAL] = DistributionFamily.NORMAL
    distribution_parameters: NormalDistributionParameters = Field(
        default=NormalDistributionParameters(), description="Parameters of the distribution"
    )


class LogNormalDistributionParameters(DistributionParametersBase):
    """
    Parameters for a log-normal distribution.

    Defined by the mean and standard deviation of the underlying normal distribution.
    """

    family: Literal[DistributionFamily.LOGNORMAL] = DistributionFamily.LOGNORMAL
    mean: float = Field(default=0, description="Mean of the distribution")
    std: float = Field(default=0, description="Standard deviation of the distribution")


class LogNormalDistribution(DistributionBase):
    """
    A log-normal probability distribution.

    Distribution where the logarithm of the variable is normally distributed.
    Always produces positive values and is right-skewed.
    """

    family: Literal[DistributionFamily.LOGNORMAL] = DistributionFamily.LOGNORMAL
    distribution_parameters: LogNormalDistributionParameters = Field(
        default=LogNormalDistributionParameters(), description="Parameters of the distribution"
    )


class UniformDistributionParameters(DistributionParametersBase):
    """
    Parameters for a uniform distribution.

    Defined by minimum and maximum bounds of the distribution.
    """

    family: Literal[DistributionFamily.UNIFORM] = DistributionFamily.UNIFORM
    min: float = Field(default=0, description="Minimum value of the distribution")
    max: float = Field(default=0, description="Maximum value of the distribution")


class UniformDistribution(DistributionBase):
    """
    A uniform probability distribution.

    All values between min and max have equal probability of being sampled.
    """

    family: Literal[DistributionFamily.UNIFORM] = DistributionFamily.UNIFORM
    distribution_parameters: UniformDistributionParameters = Field(
        default=UniformDistributionParameters(), description="Parameters of the distribution"
    )


class ExponentialDistributionParameters(DistributionParametersBase):
    """
    Parameters for an exponential distribution.

    Defined by the rate parameter (inverse of mean).
    """

    family: Literal[DistributionFamily.EXPONENTIAL] = DistributionFamily.EXPONENTIAL
    rate: float = Field(default=0, ge=0, description="Rate parameter of the distribution")


class ExponentialDistribution(DistributionBase):
    """
    An exponential probability distribution.

    Models time between events in a Poisson process. Commonly used
    for wait times and inter-event intervals.
    """

    family: Literal[DistributionFamily.EXPONENTIAL] = DistributionFamily.EXPONENTIAL
    distribution_parameters: ExponentialDistributionParameters = Field(
        default=ExponentialDistributionParameters(), description="Parameters of the distribution"
    )


class GammaDistributionParameters(DistributionParametersBase):
    """
    Parameters for a gamma distribution.

    Defined by shape (k) and rate (θ⁻¹) parameters.
    """

    family: Literal[DistributionFamily.GAMMA] = DistributionFamily.GAMMA
    shape: float = Field(default=1, ge=0, description="Shape parameter of the distribution")
    rate: float = Field(default=1, ge=0, description="Rate parameter of the distribution")


class GammaDistribution(DistributionBase):
    """
    A gamma probability distribution.

    Generalizes the exponential distribution. Used for modeling
    positive continuous variables with right-skewed distributions.
    """

    family: Literal[DistributionFamily.GAMMA] = DistributionFamily.GAMMA
    distribution_parameters: GammaDistributionParameters = Field(
        default=GammaDistributionParameters(), description="Parameters of the distribution"
    )


class BinomialDistributionParameters(DistributionParametersBase):
    """
    Parameters for a binomial distribution.

    Defined by number of trials (n) and success probability (p).
    """

    family: Literal[DistributionFamily.BINOMIAL] = DistributionFamily.BINOMIAL
    n: int = Field(default=1, ge=0, description="Number of trials")
    p: float = Field(default=0.5, ge=0, le=1, description="Probability of success")


class BinomialDistribution(DistributionBase):
    """
    A binomial probability distribution.

    Models the number of successes in a fixed number of independent
    Bernoulli trials with constant success probability.
    """

    family: Literal[DistributionFamily.BINOMIAL] = DistributionFamily.BINOMIAL
    distribution_parameters: BinomialDistributionParameters = Field(
        default=BinomialDistributionParameters(), description="Parameters of the distribution"
    )


class BetaDistributionParameters(DistributionParametersBase):
    """
    Parameters for a beta distribution.

    Defined by alpha and beta shape parameters.
    """

    family: Literal[DistributionFamily.BETA] = DistributionFamily.BETA
    alpha: float = Field(default=5, ge=0, description="Alpha parameter of the distribution")
    beta: float = Field(default=5, ge=0, description="Beta parameter of the distribution")


class BetaDistribution(DistributionBase):
    """
    A beta probability distribution.

    Continuous distribution bounded between 0 and 1. Commonly used
    for modeling probabilities and proportions.
    """

    family: Literal[DistributionFamily.BETA] = DistributionFamily.BETA
    distribution_parameters: BetaDistributionParameters = Field(
        default=BetaDistributionParameters(), description="Parameters of the distribution"
    )


class PoissonDistributionParameters(DistributionParametersBase):
    """
    Parameters for a Poisson distribution.

    Defined by the rate parameter (average number of events).
    """

    family: Literal[DistributionFamily.POISSON] = DistributionFamily.POISSON
    rate: float = Field(
        default=1, ge=0, description="Rate parameter of the Poisson process that generates the distribution"
    )


class PoissonDistribution(DistributionBase):
    """
    A Poisson probability distribution.

    Models the number of events occurring in a fixed interval of time or space
    when events occur independently at a constant rate.
    """

    family: Literal[DistributionFamily.POISSON] = DistributionFamily.POISSON
    distribution_parameters: PoissonDistributionParameters = Field(
        default=PoissonDistributionParameters(), description="Parameters of the distribution"
    )


class PdfDistributionParameters(DistributionParametersBase):
    """
    Parameters for a custom probability density function distribution.

    Defined by explicit probability values and their corresponding indices.
    Probabilities are automatically normalized to sum to 1.
    """

    family: Literal[DistributionFamily.PDF] = DistributionFamily.PDF
    pdf: List[NonNegativeFloat] = Field(default=[1], description="The probability density function")
    index: List[float] = Field(default=[0], description="The index of the probability density function")

    @field_validator("pdf")
    @classmethod
    def normalize_pdf(cls, v: List[NonNegativeFloat]) -> List[NonNegativeFloat]:
        """Normalizes the PDF values to sum to 1"""
        return [x / sum(v) for x in v]

    @model_validator(mode="after")
    def validate_matching_length(self) -> Self:
        """Ensures that pdf and index arrays have matching lengths"""
        if len(self.pdf) != len(self.index):
            raise ValueError("pdf and index must have the same length")
        return self


class PdfDistribution(DistributionBase):
    """
    A custom probability density function distribution.

    Allows defining arbitrary discrete distributions by specifying
    probability values and their corresponding indices.
    """

    family: Literal[DistributionFamily.PDF] = DistributionFamily.PDF
    distribution_parameters: PdfDistributionParameters = Field(
        default=PdfDistributionParameters(),
        description="Parameters of the distribution",
        validate_default=True,
    )


def _numeric_to_scalar(value: Any) -> Scalar | Any:
    """
    Converts numeric values to Scalar distributions.

    Enables automatic coercion of plain numbers to scalar distributions
    during validation for convenient API usage.
    """
    try:
        value = float(value)
        return Scalar(distribution_parameters=ScalarDistributionParameter(value=value))
    except (TypeError, ValueError):
        return value


Distribution = TypeAliasType(
    "Distribution",
    Annotated[
        Union[
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
        ],
        Field(discriminator="family", title="Distribution", description="Available distributions"),
        BeforeValidator(_numeric_to_scalar),
    ],
)

DistributionParameters = TypeAliasType(
    "DistributionParameters",
    Annotated[
        Union[
            ScalarDistributionParameter,
            NormalDistributionParameters,
            LogNormalDistributionParameters,
            ExponentialDistributionParameters,
            UniformDistributionParameters,
            PoissonDistributionParameters,
            BinomialDistributionParameters,
            BetaDistributionParameters,
            GammaDistributionParameters,
            PdfDistributionParameters,
        ],
        Field(discriminator="family", title="DistributionParameters", description="Parameters of the distribution"),
    ],
)
