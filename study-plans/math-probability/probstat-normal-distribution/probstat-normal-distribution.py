from scipy.stats import norm

def normal_distribution(mu: float, sigma: float, x: float) -> dict:
    """
    Returns the z-score, CDF, PDF, and one-standard-deviation probability.
    """
    z_score = (x - mu) / sigma

    
    return {
        "z_score": round(float(z_score), 4),
        "cdf": round(float(norm.cdf(x, loc=mu, scale=sigma)), 4),
        "pdf": round(float(norm.pdf(x, loc=mu, scale=sigma)), 4),
        "prob_within_1_std": round(float(norm.cdf(mu + sigma, loc=mu, scale=sigma) - norm.cdf(mu - sigma, loc=mu, scale=sigma)), 4),
    }


    