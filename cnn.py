import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from torch.autograd import Variable
from torch.utils.data import Dataset, DataLoader

EPOCHS = 50
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

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(
                in_channels=1,
                out_channels=8,
                kernel_size=3,
                stride=1,
                padding=1
            ),
            nn.ReLU(),
            nn.AvgPool2d(kernel_size=2)
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(8, 16, 3, 1, 1),
            nn.ReLU(),
            nn.AvgPool2d(2)
        )
        self.out = nn.Linear(16, 2)

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = x.view(x.size(0), -1)
        output = self.out(x)
        return output

train_data = pd.read_csv(r'train_data.csv')
x = train_data.iloc[:, : 16].to_numpy()
y = train_data['label1'].to_numpy()
x = x.reshape(len(x), 1, 4, 4)
x = torch.tensor(x, dtype=torch.float)
dataset = TrainDataset(x, y)
data_loader = DataLoader(dataset, batch_size=batch_size, num_workers=0, shuffle=True, drop_last=False)

# for batch_x, batch_y in data_loader:
#     print(batch_x.shape, batch_y.shape)

cnn = CNN()
print(cnn)

optimizer = torch.optim.Adam(cnn.parameters(), lr=0.05)
loss_func = nn.CrossEntropyLoss()

for epoch in range(EPOCHS):
    for i, (x, y) in enumerate(data_loader):
        output = cnn(x)
        loss = loss_func(output, y)
        # print(output)
        print('Epoch: ' + str(epoch) + ' i=' + str(i) + ' loss=' + str(loss))
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

correct = 0
total = 0
for (x, y) in data_loader:
    output = cnn(x)
    # prediction = torch.max(output, dim=1)
    # total += y.size(0)
    for i in range(len(output)):
        p1 = output[i][0]
        p2 = output[i][1]
        if (p1 > p2):
            val = 0
        else:
            val = 1
        if (val == y[i]):
            correct += 1
    total += len(y)
    # print(y, val)
print(correct, total)