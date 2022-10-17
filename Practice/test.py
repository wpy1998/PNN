import numpy as np
import pandas as pd

train_data = pd.read_csv(r'data.csv')
x = train_data.iloc[:, : 100].to_numpy()
y = train_data['label'].to_numpy()
x = x.reshape(len(x), 1, 10, 10)
print(x[1][0])