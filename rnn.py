import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import pandas as pd

class TorchDataset(Dataset):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getitem__(self, item):
        return self.x[item], self.y[item]

    def __len__(self):
        return self.x.shape[0]

EPOCHS = 50
batch_size = 50

train_data = pd.read_csv(r'train_data.csv')
x = train_data.iloc[:, : 16].to_numpy()
y = train_data['label1'].to_numpy()
x = x.reshape(len(x), 4, 4)
x = torch.tensor(x, dtype=torch.float)
dataset = TorchDataset(x, y)
data_loader = DataLoader(dataset, batch_size=batch_size, num_workers=0, shuffle=True, drop_last=False)

class RNN(nn.Module):
    def __init__(self):
        super(RNN, self).__init__()

        self.rnn = nn.LSTM(
            input_size=4,
            hidden_size=64,
            num_layers=1,
            batch_first=True
        )

        self.out = nn.Linear(64, 2)

    def forward(self, x):
        # x shape (batch, time_step, input_size)
        # r_out shape (batch, time_step, output_size)
        # h_n shape (n_layers, batch, hidden_size)
        # h_c shape (n_layers, batch, hidden_size)
        r_out, (h_n, h_c) = self.rnn(x, None)   # None represents zero initial hidden state
        # choose r_out at the last time step
        out = self.out(r_out[:, -1, :])
        return out

rnn = RNN()
print(rnn)
optimizer = torch.optim.Adam(rnn.parameters(), lr=0.05)
loss_func = nn.CrossEntropyLoss()
for epoch in range(EPOCHS):
    for step, (b_x, b_y) in enumerate(data_loader):
        b_x = b_x.view(-1, 4, 4)
        output = rnn(b_x)
        # print(output)
        loss = loss_func(output, b_y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        print('loss = ', loss)

correct = 0
total = 0
for (x, y) in data_loader:
    output = rnn(x)
    # prediction = torch.max(output, dim=1)
    # total += y.size(0)
    for i in range(len(output)):
        p1 = output[i][0]
        p2 = output[i][1]
        if(p1 > p2):
            val = 0
        else:
            val = 1
        if(val == y[i]):
            correct += 1
    total += len(y)
    # print(y, val)
print(correct, total)