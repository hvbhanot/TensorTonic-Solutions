from math import exp, factorial

def poisson_distribution(lam: float, max_k: int) -> list:
    """
    Returns the PMF list, cumulative probability, and zero-event probability.
    """

    pmf = []
    cdf = 0.0
    for k in range(max_k+1):
   
        P_X_k = ((lam**k) * (exp(-lam))) / factorial(k)
        pmf.append(P_X_k)
        cdf += P_X_k

    return [pmf, cdf, pmf[0]]