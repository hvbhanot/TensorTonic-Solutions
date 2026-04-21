import torch

def reshape_tensor(x, op):
    """
    Returns: list
    """
    x = torch.tensor(x,dtype=torch.float)

    if op == 'flatten':
        return x.flatten().tolist()
    elif op == 'squeeze':
        return x.squeeze().tolist()
    else:
        return x.T.tolist()