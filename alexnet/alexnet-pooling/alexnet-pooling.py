import numpy as np

def max_pool2d(x: np.ndarray, kernel_size: int = 3, stride: int = 2) -> np.ndarray:
    """
    Apply 2D max pooling (shape simulation).
    """

    inp_shape = x.shape[1]
    shape = int(np.floor((inp_shape - kernel_size) / stride) + 1)

    output = np.zeros((x.shape[0] , shape, shape , x.shape[3]))

    return output