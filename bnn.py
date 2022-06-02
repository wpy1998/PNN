import torch
import torch.nn as nn
import pandas as pd
import numpy as np
from torch.utils.data import Dataset

EPOCHS = 1
batch_size = 50

# dataset
class TrainDataset(Dataset):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getitem__(self, item):
        return self.x[item], self.y[item]

    def __len__(self):
        return self.x.shape[0]