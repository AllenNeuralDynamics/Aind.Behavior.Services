import unittest

import numpy as np

from aind_behavior_services.task.distributions import (
    BetaDistribution,
    BetaDistributionParameters,
    BinomialDistribution,
    BinomialDistributionParameters,
    ExponentialDistribution,
    ExponentialDistributionParameters,
    GammaDistribution,
    GammaDistributionParameters,
    LogNormalDistribution,
    LogNormalDistributionParameters,
    NormalDistribution,
    NormalDistributionParameters,
    PdfDistribution,
    PdfDistributionParameters,
    PoissonDistribution,
    PoissonDistributionParameters,
    Scalar,
    ScalarDistributionParameter,
    ScalingParameters,
    TruncationParameters,
    UniformDistribution,
    UniformDistributionParameters,
)
from aind_behavior_services.task.distributions_utils import (
    _apply_scaling,
    _apply_truncation,
    _sample_raw,
    draw_sample,
    draw_samples,
)


def create_rng(seed=None):
    return np.random.default_rng(int(seed) if seed is not None else None)


class TestCreateRng(unittest.TestCase):
    """Tests for create_rng function."""

    def test_create_rng_without_seed(self):
        rng = create_rng()
        self.assertIsInstance(rng, np.random.Generator)

    def test_create_rng_with_int_seed(self):
        rng1 = create_rng(42)
        rng2 = create_rng(42)
        self.assertEqual(rng1.random(), rng2.random())

    def test_create_rng_with_float_seed(self):
        rng1 = create_rng(42.7)
        rng2 = create_rng(42)
        self.assertEqual(rng1.random(), rng2.random())

    def test_different_seeds_produce_different_sequences(self):
        rng1 = create_rng(42)
        rng2 = create_rng(43)
        self.assertNotEqual(rng1.random(), rng2.random())


class TestApplyScaling(unittest.TestCase):
    """Tests for _apply_scaling function."""

    def test_no_scaling_params(self):
        result = _apply_scaling(np.array([5.0]), None)
        self.assertEqual(result[0], 5.0)

    def test_identity_scaling(self):
        params = ScalingParameters(scale=1, offset=0)
        result = _apply_scaling(np.array([5.0]), params)
        self.assertEqual(result[0], 5.0)

    def test_scale_only(self):
        params = ScalingParameters(scale=2, offset=0)
        result = _apply_scaling(np.array([5.0]), params)
        self.assertEqual(result[0], 10.0)

    def test_offset_only(self):
        params = ScalingParameters(scale=1, offset=3)
        result = _apply_scaling(np.array([5.0]), params)
        self.assertEqual(result[0], 8.0)

    def test_scale_and_offset(self):
        params = ScalingParameters(scale=2, offset=3)
        result = _apply_scaling(np.array([5.0]), params)
        self.assertEqual(result[0], 13.0)

    def test_negative_scale(self):
        params = ScalingParameters(scale=-1, offset=10)
        result = _apply_scaling(np.array([5.0]), params)
        self.assertEqual(result[0], 5.0)

    def test_vectorized(self):
        params = ScalingParameters(scale=2, offset=1)
        result = _apply_scaling(np.array([1.0, 2.0, 3.0]), params)
        np.testing.assert_array_equal(result, np.array([3.0, 5.0, 7.0]))


class TestApplyTruncation(unittest.TestCase):
    """Tests for _apply_truncation function."""

    def test_no_truncation_params(self):
        result = _apply_truncation(np.array([5.0]), None)
        self.assertEqual(result[0], 5.0)

    def test_truncation_disabled_when_min_equals_max(self):
        params = TruncationParameters(min=0, max=0)
        result = _apply_truncation(np.array([5.0]), params)
        self.assertEqual(result[0], 5.0)

    def test_value_within_bounds(self):
        params = TruncationParameters(min=0, max=10)
        result = _apply_truncation(np.array([5.0]), params)
        self.assertEqual(result[0], 5.0)

    def test_clamp_to_min(self):
        params = TruncationParameters(min=0, max=10)
        result = _apply_truncation(np.array([-5.0]), params)
        self.assertEqual(result[0], 0.0)

    def test_clamp_to_max(self):
        params = TruncationParameters(min=0, max=10)
        result = _apply_truncation(np.array([15.0]), params)
        self.assertEqual(result[0], 10.0)

    def test_vectorized(self):
        params = TruncationParameters(min=0, max=10)
        result = _apply_truncation(np.array([-5.0, 5.0, 15.0]), params)
        np.testing.assert_array_equal(result, np.array([0.0, 5.0, 10.0]))


class TestSampleRawScalar(unittest.TestCase):
    """Tests for sampling from Scalar distribution."""

    def test_scalar_returns_constant_value(self):
        dist = Scalar(distribution_parameters=ScalarDistributionParameter(value=42.5))
        rng = create_rng(0)
        samples = _sample_raw(dist, rng, 10)
        self.assertTrue(np.all(samples == 42.5))


class TestSampleRawNormal(unittest.TestCase):
    """Tests for sampling from Normal distribution."""

    def test_normal_mean_and_std(self):
        dist = NormalDistribution(distribution_parameters=NormalDistributionParameters(mean=10, std=2))
        rng = create_rng(42)
        samples = _sample_raw(dist, rng, 10000)
        self.assertAlmostEqual(np.mean(samples), 10, delta=0.1)
        self.assertAlmostEqual(np.std(samples), 2, delta=0.1)


class TestSampleRawLogNormal(unittest.TestCase):
    """Tests for sampling from LogNormal distribution."""

    def test_lognormal_positive_values(self):
        dist = LogNormalDistribution(distribution_parameters=LogNormalDistributionParameters(mean=0, std=1))
        rng = create_rng(42)
        samples = _sample_raw(dist, rng, 100)
        self.assertTrue(np.all(samples > 0))


class TestSampleRawUniform(unittest.TestCase):
    """Tests for sampling from Uniform distribution."""

    def test_uniform_within_bounds(self):
        dist = UniformDistribution(distribution_parameters=UniformDistributionParameters(min=5, max=15))
        rng = create_rng(42)
        samples = _sample_raw(dist, rng, 1000)
        self.assertTrue(np.all((samples >= 5) & (samples <= 15)))
        self.assertAlmostEqual(np.mean(samples), 10, delta=0.5)


class TestSampleRawExponential(unittest.TestCase):
    """Tests for sampling from Exponential distribution."""

    def test_exponential_positive_values(self):
        dist = ExponentialDistribution(distribution_parameters=ExponentialDistributionParameters(rate=2))
        rng = create_rng(42)
        samples = _sample_raw(dist, rng, 1000)
        self.assertTrue(np.all(samples >= 0))
        self.assertAlmostEqual(np.mean(samples), 0.5, delta=0.05)

    def test_exponential_zero_rate(self):
        dist = ExponentialDistribution(distribution_parameters=ExponentialDistributionParameters(rate=0))
        rng = create_rng(42)
        samples = _sample_raw(dist, rng, 10)
        self.assertTrue(np.all(samples == 0.0))


class TestSampleRawGamma(unittest.TestCase):
    """Tests for sampling from Gamma distribution."""

    def test_gamma_positive_values(self):
        dist = GammaDistribution(distribution_parameters=GammaDistributionParameters(shape=2, rate=1))
        rng = create_rng(42)
        samples = _sample_raw(dist, rng, 1000)
        self.assertTrue(np.all(samples >= 0))
        self.assertAlmostEqual(np.mean(samples), 2, delta=0.15)

    def test_gamma_zero_rate(self):
        dist = GammaDistribution(distribution_parameters=GammaDistributionParameters(shape=2, rate=0))
        rng = create_rng(42)
        samples = _sample_raw(dist, rng, 10)
        self.assertTrue(np.all(samples == 0.0))


class TestSampleRawBeta(unittest.TestCase):
    """Tests for sampling from Beta distribution."""

    def test_beta_within_unit_interval(self):
        dist = BetaDistribution(distribution_parameters=BetaDistributionParameters(alpha=2, beta=5))
        rng = create_rng(42)
        samples = _sample_raw(dist, rng, 1000)
        self.assertTrue(np.all((samples >= 0) & (samples <= 1)))
        expected_mean = 2 / 7
        self.assertAlmostEqual(np.mean(samples), expected_mean, delta=0.02)


class TestSampleRawBinomial(unittest.TestCase):
    """Tests for sampling from Binomial distribution."""

    def test_binomial_integer_values(self):
        dist = BinomialDistribution(distribution_parameters=BinomialDistributionParameters(n=10, p=0.5))
        rng = create_rng(42)
        samples = _sample_raw(dist, rng, 1000)
        self.assertTrue(np.all((samples >= 0) & (samples <= 10)))
        self.assertTrue(np.all(samples == samples.astype(int)))
        self.assertAlmostEqual(np.mean(samples), 5, delta=0.2)


class TestSampleRawPoisson(unittest.TestCase):
    """Tests for sampling from Poisson distribution."""

    def test_poisson_non_negative_integers(self):
        dist = PoissonDistribution(distribution_parameters=PoissonDistributionParameters(rate=3))
        rng = create_rng(42)
        samples = _sample_raw(dist, rng, 1000)
        self.assertTrue(np.all(samples >= 0))
        self.assertTrue(np.all(samples == samples.astype(int)))
        self.assertAlmostEqual(np.mean(samples), 3, delta=0.2)


class TestSampleRawPdf(unittest.TestCase):
    """Tests for sampling from PDF distribution."""

    def test_pdf_samples_from_index(self):
        dist = PdfDistribution(
            distribution_parameters=PdfDistributionParameters(pdf=[0.25, 0.5, 0.25], index=[1, 2, 3])
        )
        rng = create_rng(42)
        samples = _sample_raw(dist, rng, 1000)
        self.assertTrue(np.all(np.isin(samples, [1, 2, 3])))
        count_2 = np.sum(samples == 2)
        self.assertGreater(count_2, 400)

    def test_pdf_single_value(self):
        dist = PdfDistribution(distribution_parameters=PdfDistributionParameters(pdf=[1], index=[42]))
        rng = create_rng(0)
        samples = _sample_raw(dist, rng, 10)
        self.assertTrue(np.all(samples == 42))


class TestDrawSample(unittest.TestCase):
    """Tests for the main draw_sample function."""

    def test_draw_sample_no_transformations(self):
        dist = Scalar(distribution_parameters=ScalarDistributionParameter(value=10))
        self.assertEqual(draw_sample(dist), 10)

    def test_draw_sample_with_scaling(self):
        dist = NormalDistribution(
            distribution_parameters=NormalDistributionParameters(mean=5, std=0),
            scaling_parameters=ScalingParameters(scale=2, offset=1),
        )
        rng = create_rng(42)
        self.assertEqual(draw_sample(dist, rng), 11)

    def test_draw_sample_with_clamp_truncation(self):
        dist = NormalDistribution(
            distribution_parameters=NormalDistributionParameters(mean=100, std=0),
            truncation_parameters=TruncationParameters(truncation_mode="clamp", min=0, max=10),
        )
        rng = create_rng(42)
        self.assertEqual(draw_sample(dist, rng), 10)

    def test_draw_sample_with_exclude_truncation(self):
        dist = UniformDistribution(
            distribution_parameters=UniformDistributionParameters(min=5, max=8),
            truncation_parameters=TruncationParameters(truncation_mode="exclude", min=0, max=10),
        )
        rng = create_rng(42)
        sample = draw_sample(dist, rng)
        self.assertGreaterEqual(sample, 0)
        self.assertLessEqual(sample, 10)

    def test_draw_sample_exclude_resamples_until_valid(self):
        dist = UniformDistribution(
            distribution_parameters=UniformDistributionParameters(min=0, max=20),
            truncation_parameters=TruncationParameters(truncation_mode="exclude", min=5, max=15),
        )
        rng = create_rng(42)
        samples = draw_samples(dist, 100, rng)
        self.assertTrue(np.all((samples >= 5) & (samples <= 15)))

    def test_draw_sample_scaling_then_truncation(self):
        dist = NormalDistribution(
            distribution_parameters=NormalDistributionParameters(mean=5, std=0),
            scaling_parameters=ScalingParameters(scale=10, offset=0),
            truncation_parameters=TruncationParameters(truncation_mode="clamp", min=0, max=30),
        )
        rng = create_rng(42)
        self.assertEqual(draw_sample(dist, rng), 30)

    def test_draw_sample_truncation_disabled_when_min_equals_max(self):
        dist = NormalDistribution(
            distribution_parameters=NormalDistributionParameters(mean=100, std=0),
            truncation_parameters=TruncationParameters(truncation_mode="clamp", min=0, max=0),
        )
        rng = create_rng(42)
        self.assertEqual(draw_sample(dist, rng), 100)


class TestDrawSamples(unittest.TestCase):
    """Tests for draw_samples function."""

    def test_draw_samples_returns_correct_count(self):
        dist = Scalar(distribution_parameters=ScalarDistributionParameter(value=5))
        samples = draw_samples(dist, 100)
        self.assertEqual(len(samples), 100)

    def test_draw_samples_returns_ndarray(self):
        dist = Scalar(distribution_parameters=ScalarDistributionParameter(value=5))
        samples = draw_samples(dist, 100)
        self.assertIsInstance(samples, np.ndarray)

    def test_draw_samples_reproducible_with_seed(self):
        dist = NormalDistribution(distribution_parameters=NormalDistributionParameters(mean=0, std=1))
        rng1 = create_rng(42)
        rng2 = create_rng(42)
        samples1 = draw_samples(dist, 10, rng1)
        samples2 = draw_samples(dist, 10, rng2)
        np.testing.assert_array_equal(samples1, samples2)


class TestIntegration(unittest.TestCase):
    """Integration tests combining multiple features."""

    def test_full_pipeline_normal_with_transformations(self):
        dist = NormalDistribution(
            distribution_parameters=NormalDistributionParameters(mean=0, std=1),
            scaling_parameters=ScalingParameters(scale=2, offset=5),
            truncation_parameters=TruncationParameters(truncation_mode="clamp", min=0, max=10),
        )
        rng = create_rng(42)
        samples = draw_samples(dist, 1000, rng)
        self.assertTrue(np.all((samples >= 0) & (samples <= 10)))

    def test_exclude_mode_fallback_for_impossible_bounds(self):
        dist = NormalDistribution(
            distribution_parameters=NormalDistributionParameters(mean=1000, std=0.001),
            truncation_parameters=TruncationParameters(truncation_mode="exclude", min=0, max=1),
        )
        rng = create_rng(42)
        sample = draw_sample(dist, rng)
        self.assertEqual(sample, 1)

    def test_numeric_coercion_with_sampling(self):
        from aind_behavior_services.task.distributions import _numeric_to_scalar

        scalar_dist = _numeric_to_scalar(42.5)
        sample = draw_sample(scalar_dist)
        self.assertEqual(sample, 42.5)


if __name__ == "__main__":
    unittest.main()
