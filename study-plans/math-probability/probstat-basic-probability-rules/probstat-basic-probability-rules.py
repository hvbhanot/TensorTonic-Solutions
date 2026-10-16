def basic_probability(p_a: float, p_b: float, p_a_and_b: float) -> list:
    """
    Returns four rounded probability values in the required order.
    """
    return [(p_a+p_b-p_a_and_b) , (1-p_a), (1-p_b), (p_a-p_a_and_b)]