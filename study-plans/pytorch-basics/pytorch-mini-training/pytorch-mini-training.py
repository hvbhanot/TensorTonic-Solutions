import torch
import torch.nn as nn
import numpy as np

def train_epoch(model, dataloader, criterion, optimizer):

    """

    Returns: average loss over all batches (float)

    """

    batch_loss = []

    for x,y in dataloader:

        yhat = model(x)

        loss = criterion(yhat, y)

        batch_loss.append(loss.item())

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()

        

    cost = np.mean(batch_loss)

    return cost