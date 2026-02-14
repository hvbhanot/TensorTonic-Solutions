def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    
    L = np.sqrt(6/(fan_in))
                
    arr = np.array(W)
    output = arr * (2*L) - L
      
    return output.tolist()