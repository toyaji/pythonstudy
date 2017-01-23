import numpy as np
import pandas as pd
import h5py
import matplotlib.pyplot as plt


data = h5py.File(r'C:\Users\user\Downloads\kospi.hdf5', 'r')

grp = data.create_group('mynewGroup')

