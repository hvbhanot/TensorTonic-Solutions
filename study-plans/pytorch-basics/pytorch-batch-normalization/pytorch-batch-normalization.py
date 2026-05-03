import torch

def batch_norm(X, gamma, beta, eps=1e-5):
    """
    Returns: tensor of shape (N, D), the batch-normalized output
    """
    mean = torch.mean(X, dim=0)
    var = torch.var(X, dim=0, unbiased=False) # Bessels Correction

    Xhat = (X-mean)/torch.sqrt(var + eps)

    Y = gamma*Xhat + beta

    return Y
