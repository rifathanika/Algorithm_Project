import numpy as np

class ProbabilityModel:
    """
    Computes likelihoods or probabilities for different sensor states.
    """
    def __init__(self, mean: float, std: float):
        self.mean = mean
        self.std = std

    def probability_within_range(self, value_range):
        """
        Computes the probability that a value from a normal distribution falls within a range.
        value_range: tuple (low, high)
        """
        low, high = value_range
        p_low = self._cdf(low)
        p_high = self._cdf(high)
        return p_high - p_low

    def _cdf(self, x):
        return 0.5 * (1 + np.math.erf((x - self.mean) / (self.std * np.sqrt(2))))
