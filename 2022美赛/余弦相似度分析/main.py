import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data1 = np.array(pd.read_csv('ObjV03.csv', names=['1', '2', '3', '4', '5', '6']))
data2 = np.array(pd.read_csv('ObjV02.csv', names=['1', '2', '3', '4', '5', '6']))


def cosine(A, B):
    # AB = A * B.transpose()
    # A_norm = np.sqrt(np.multiply(A, A).sum(axis=1))
    # B_norm = np.sqrt(np.multiply(B, B).sum(axis=1))

    return np.sum(A * B, axis=1) / (np.sqrt(np.sum(A ** 2, axis=1)) * np.sqrt(np.sum(B ** 2, axis=1)))


a = cosine(data1,data2)
print(a.mean())
plt.plot(range(0,100),a)
plt.show()
