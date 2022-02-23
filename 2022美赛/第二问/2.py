import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('iron_data.csv')

c = data.research * data.GDP * 0.01 * 1
s = c * 233.57 / c.sum()
b = 122.47

print(c * 0.02)

w = b * s * 1000000 - c * 0.02

p = w / w.sum()
plt.pie(p,labels=data.country,autopct='%1.2f%%')
plt.axis('equal')
plt.show()

print(p)
