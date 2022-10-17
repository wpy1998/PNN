import scipy.io as sio

dataFile = 'Data/Normal Baseline Data/97.mat'
data = sio.loadmat(dataFile)
print(data)
print(len(data['X097_FE_time']))
for i in range(len(data['X097_FE_time'])):
    print('epoch: ' + str(i), data['X097_FE_time'][i])