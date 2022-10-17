import torch
import torch.nn as nn
import pandas as pd
import numpy as np
from torch.autograd import Variable
from torch.utils.data import Dataset, DataLoader

EPOCHS = 50
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

class AutoEncoder(nn.Module):
    def __init__(self):
        super(AutoEncoder, self).__init__()
        self.encoder = nn.Sequential(
            nn.Linear(4 * 4, 8),
            nn.Tanh(),
            nn.Linear(8, 3)
        )
        self.decoder = nn.Sequential(
            nn.Linear(3, 8),
            nn.Tanh(),
            nn.Linear(8, 16),
            nn.Sigmoid()
        )

    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return encoded, decoded

autoEncoder = AutoEncoder()
optimizer = torch.optim.Adam(autoEncoder.parameters(), lr=0.005)
loss_func = nn.MSELoss()

train_data = pd.read_csv(r'train_data.csv')
x = train_data.iloc[:, : 16].to_numpy()
y = train_data['label1'].to_numpy()
x = x.reshape(len(x), 1, 16)
x = torch.tensor(x, dtype=torch.float)
y = torch.tensor(y, dtype=torch.float)
dataset = TrainDataset(x, y)
data_loader = DataLoader(dataset, batch_size=batch_size, num_workers=0, shuffle=True, drop_last=False)

for epoch in range(EPOCHS):
    for step, (x, y) in enumerate(data_loader):
        b_x = x.view(-1, 16)
        b_y = x.view(-1, 16)
        b_label = Variable(y)
        encoded, decoded = autoEncoder(b_x)
        loss = loss_func(decoded, b_y)
        # print(output)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        print('Epoch: ' + str(epoch) + ' step=' + str(step) + ' loss=' + str(loss))