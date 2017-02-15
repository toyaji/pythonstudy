import numpy as np, pandas as pd

import codecs

name = [x for x in range(61)]

with codecs.open(r'C:\Users\Paul\Downloads\WDI_csv\WDI_Data.csv', 'r') as file:
    data = pd.read_csv(file, header=1, names=name)
    print(data.head())

    data2 = pd.read_csv(file, na_values=0)
    print(data2.head())