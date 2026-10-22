import numpy as np

def mle_normal(data: list) -> dict:
    """
    Returns the normal-distribution MLEs mu_mle and sigma_mle.
    """
    data = np.asarray(data,dtype=float)

    mean = np.mean(data)

    sigma_hat = np.sqrt(np.mean( pow(data-mean,2)))

    return {"mu_mle":round(mean,4),
            "sigma_mle":round(sigma_hat,4)}
