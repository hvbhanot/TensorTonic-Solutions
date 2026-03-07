def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """

    global_min = x0

    
    for _ in range(steps):
     deriv =  2*a*global_min + b
     global_min = global_min - lr*deriv

    return global_min
  