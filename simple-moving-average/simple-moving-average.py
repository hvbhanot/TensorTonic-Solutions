def simple_moving_average(values, window_size):
    """
    Compute the simple moving average of the given values.
    """
    output = []

    for i in range(len(values) - window_size + 1):

      sum = 0
      counter = i
      for j in range(window_size):
        sum += values[counter]
        counter += 1

      output.append(sum/window_size)  

    return output 