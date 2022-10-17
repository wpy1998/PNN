import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from torch.autograd import Variable
from torch.utils.data import Dataset, DataLoader

EPOCHS = 30
batch_size = 1

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
                kernel_size=5,
                stride=1,
                padding=1
            ),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(8, 16, 5, 1, 1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        self.out = nn.Linear(16, 2)

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = x.view(x.size(0), -1)
        output = self.out(x)
        return output

train_data = pd.read_csv(r'data.csv')
x = train_data.iloc[:, : 100].to_numpy()
y = train_data['label'].to_numpy()
print(y)
x = x.reshape(len(x), 1, 10, 10)
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
    for step, (x, y) in enumerate(data_loader):
        b_x = Variable(x)
        b_y = Variable(y)
        output = cnn(b_x)
        loss = loss_func(output, b_y)
        # print(output)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        print('Epoch: ' + str(epoch) + ' step=' + str(step) + ' loss=' + str(loss))

correct = 0
total = 0
for (x, y) in data_loader:
    output = cnn(x)
    for i in range(len(output)):
        print(output[i][0], output[i][1])