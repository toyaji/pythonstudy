import numpy as np
import pandas as pd
import h5py
import matplotlib.pyplot as plt

file = r'C:\Users\user\Downloads\L-L1_LOSC_4_V1-931110912-4096.hdf5'

data = h5py.File(file, 'r')

# grp = data.create_group('mynewGroup')
# 그룹 만들어내는 메서드

# there are three basic type of items in HDF5 file: File, Group, and Dataset.
# HDF5 파일에 요렇게 세가지 구성요소가 있음

group = data['strain']

isGroup = isinstance(group, h5py.Group)
print(isGroup)
# 현지 객체가 그룹인지, 데이터셋인지 확인하는 방법

for x in group.items():
    print(x)

# dataset = list(group['Strain'])
# 위에 방법으로 하면 너무 오래도는듯?

dataset = data['strain/Strain']

# key 값이 path 포함이어야하고 역슬래쉬로 되어 있어야함. 이거 진짜 헷갈림 ㅠ

isDataset = isinstance(dataset, h5py.Dataset)
print(isDataset)

nparr = np.array(dataset)
print(nparr.shape)
print(nparr[2:100])

# 지금 다운받은 데이터는 내용이 비어있는듯

num_samples = 10000
time = np.arange(0, 1, 1/num_samples)

plt.plot(time, nparr[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()


