from math import comb

def binomial_distribution(n: int, p: float, threshold: int) -> dict:
    """
    Returns the PMF, mean, variance, and probability at least threshold.
    """
    pmf = [comb(n, k) * p ** k * (1.0 - p) ** (n - k) for k in range(n + 1)]

       
    return {
        "pmf": [round(float(value), 4) for value in pmf],
        "mean": round(float(n * p), 4),
        "variance": round(float(n * p * (1.0 - p)), 4),
        "prob_at_least": round(float(sum(pmf[threshold:])), 4),
    }
