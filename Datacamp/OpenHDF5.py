import numpy as np
import pandas as pd
import h5py
import matplotlib.pyplot as plt

file = r'C:\Users\user\Downloads\L-L1_LOSC_4_V1-931110912-4096.hdf5'

data = h5py.File(file, 'r')

# grp = data.create_group('mynewGroup')
# 그룹 만들어내는 메서드

group = data['strain'].keys()

for key in data:
    print(key)

strain = np.array(group['Strain'].values())
for key in strain:
    print(key)


"""
num_samples = 10000
time = np.arange(0, 1, 1/num_samples)

plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()
"""

