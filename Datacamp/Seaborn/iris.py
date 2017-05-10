import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
versicolor_petal_length = iris.data[50:99, 2]

sns.set()

def simple_hist(data):
    data = versicolor_petal_length
    _ = plt.hist(data)
    _ = plt.grid(True)
    _ = plt.xlabel('petal length (cm)')
    _ = plt.ylabel('count')

    plt.show()


def ecdf(data):
    n = len(data)
    x = np.sort(data)
    y = np.arange(1, n+1) / n
    return x, y

if __name__ == '__main__':
    x, y = ecdf(data=versicolor_petal_length)
    plt.plot(x, y, marker='.')
    plt.margins(0.02)     # 차트 변두리에 마준 둘 퍼센티지...
    plt.ylabel('Empirical Cumulative Distribute Function')
    plt.show()