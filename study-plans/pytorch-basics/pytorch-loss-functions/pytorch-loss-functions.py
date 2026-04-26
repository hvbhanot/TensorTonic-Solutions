import torch

def compute_loss(pred, target, method, delta=1.0):
    """
    Returns: float, the mean loss value
    """

    pred = torch.tensor(pred, dtype=torch.float)
    target = torch.tensor(target, dtype=torch.float)

    if method == "mse":
        lossFunc = torch.nn.MSELoss()
        return lossFunc(pred, target)

    elif method == "cross_entropy":
        lossFunc = torch.nn.CrossEntropyLoss()
        return lossFunc(pred, target.long())

    else:
        lossFunc = torch.nn.HuberLoss(delta=delta)
        return lossFunc(pred, target)
        
        