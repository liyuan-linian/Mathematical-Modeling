import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
'''
x = np.array([7, 8, 9, 10, 11])
y = np.array([154.44, 148, 139, 122.67, 89])


def func(x, a, b):
    return (3.918 * x + 123.3) * (1 - a * np.exp(b * x))

#return (0.05779 * x ** 2 - 0.1274 * x + 127.4
plt.scatter(x, y, color='orange', label='price')

popt, pcov = curve_fit(func, x, y)

y1 = [func(i, popt[0], popt[1]) for i in np.linspace(7, 12, 500)]
plt.plot(np.linspace(7, 12, 500), y1, color='seagreen')
print(popt[0], popt[1])
plt.show()
'''
x = [0,1,2,3,4,5,6,7]
y = [127,130,126,134,136,141,148,154.44]
coef = np.polyfit(x,y,1)
poly_fit = np.poly1d(coef)
print(poly_fit)
x1 = np.linspace(0,7,800)
plt.plot(x1,poly_fit(x1),color ='skyblue')
plt.scatter(x,y,color='orange',label='price')
plt.show()


