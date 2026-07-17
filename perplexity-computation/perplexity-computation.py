def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    
    prob_distributions = np.asarray(prob_distributions, dtype=float)
    actual_tokens = np.asarray(actual_tokens, dtype=int)

    N = len(actual_tokens)
    p = prob_distributions[np.arange(N), actual_tokens]

    p = np.clip(p, 1e-12, 1.0)

    cross_entropy = -np.mean(np.log(p))

    return round(np.exp(cross_entropy), 4)