import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch import optim

EPOCH = 1               # train the training data n times, to save time, we just train 1 epoch
BATCH_SIZE = 50

train_data = pd.read_csv(r'train_data.csv')
train_data = np.array(train_data)
x = torch.from_numpy(train_data)
x = torch.reshape(x, (len(x), 1, 4, 4))
x = x.to(torch.float32)

train_result = pd.read_csv(r'train_result.csv')
train_result = np.array(train_result)
y = torch.from_numpy(train_result)

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(
                in_channels=1,
                out_channels=4,
                kernel_size=3,
                stride=1,
                padding=1
            ),
            nn.ReLU(),
            nn.MaxPool2d(2) # 4 * 3 * 3
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(4, 2, 3, 1, 1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        self.out = nn.Linear(2, 1)

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        output = self.out(x)
        return output, x

cnn = CNN()
print(cnn)

optimizer = torch.optim.Adam(cnn.parameters(), lr=0.05)
loss_func = nn.CrossEntropyLoss()

for epoch in range(EPOCH):
    for i in range(len(x)):
        output = cnn(x[i])[0]
        loss = loss_func(output, y[i])
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        print(loss)