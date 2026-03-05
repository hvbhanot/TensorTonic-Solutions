def exponential_moving_average(values, alpha):
    """
    Compute the exponential moving average of the given values.
    """
    
    output = []
    output.append(values[0])

    for i in range(1,len(values)):
      avg = alpha * values[i] + (1-alpha) * output[i-1]

      output.append(avg)

    return output  