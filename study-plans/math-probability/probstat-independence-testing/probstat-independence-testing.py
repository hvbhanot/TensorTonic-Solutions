def independence_test(p_a, p_b, p_a_and_b):
    """
    Returns: dict with 'p_a_times_p_b' (float) and 'is_independent' (bool).
    """

    solution = {
        "p_a_times_p_b" : round(p_a*p_b,4),
        "is_independent" : True if (round(p_a*p_b,4) == p_a_and_b) else False
    }
    
    return solution
