def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """

    min = x0

    for i in range(steps):
      min = min - lr*((2*a*min) + (b))


    return min