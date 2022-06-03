import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from torch.autograd import Variable
from torch.utils.data import Dataset, DataLoader

EPOCHS = 30
batch_size = 100

# dataset
class TrainDataset(Dataset):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getitem__(self, item):
        return self.x[item], self.y[item]

    def __len__(self):
        return self.x.shape[0]

train_data = pd.read_csv(r'train_data.csv')
x = train_data.iloc[:, : 16].to_numpy()
y = train_data['label1'].to_numpy()
x = x.reshape(len(x), 1, 4, 4)
x = torch.tensor(x, dtype=torch.float)
y = torch.tensor(y, dtype=torch.float)
dataset = TrainDataset(x, y)
data_loader = DataLoader(dataset, batch_size=batch_size, num_workers=0, shuffle=True, drop_last=False)