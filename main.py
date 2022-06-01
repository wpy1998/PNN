import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from torch.autograd import Variable
from torch.utils.data import Dataset, DataLoader

EPOCHS = 1
batch_size = 5

#dataset
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
                out_channels=4,
                kernel_size=3,
                stride=1,
                padding=1
            ),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)
        )
        # self.conv2 = nn.Sequential(
        #     nn.Conv2d(4, 2, 3, 1, 1),
        #     nn.ReLU(),
        #     nn.MaxPool2d(2)
        # )
        self.out = nn.Linear(4 * 2 * 2, 4)

    def forward(self, x):
        x = self.conv1(x)
        # x = self.conv2(x)
        x = x.view(x.size(0), -1)
        output = self.out(x)
        return output

train_data = pd.read_csv(r'train_data.csv')
x = train_data.iloc[:, : 16].to_numpy()
x = x.reshape(len(x), 1, 4, 4)
y = train_data['label1'].to_numpy()
x = torch.from_numpy(x)
x = x.to(torch.double)
y = torch.from_numpy(y)
y = y.to(torch.double)
dataset = TrainDataset(x, y)
data_loader = DataLoader(dataset, batch_size=batch_size, num_workers=0, shuffle=True, drop_last=False)

# for batch_x, batch_y in data_loader:
#     print(batch_x.shape, batch_y.shape)

cnn = CNN()
print(cnn)

optimizer = torch.optim.Adam(cnn.parameters(), lr=0.05)
loss_func = nn.CrossEntropyLoss()

for epoch in range(5):
    for i, (x, y) in enumerate(data_loader):
        output = cnn(x)
        loss = loss_func(output, y)
        print('Epoch: ' + str(epoch) + ' i=' + str(i) + ' loss=' + str(loss))
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()