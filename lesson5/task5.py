import itertools
import matplotlib.pyplot as plt
import numpy as np


# Задача регрессии
# Сгенерируем случайную выборку из 100 точек
n = 100
r = 0.9
x = np.random.rand(n)
y = r * x + (1 - r) * np.random.rand(n)
plt.plot(x, y, 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
#plt.show()
plt.savefig('task5.png')
c = np.corrcoef(x, y)
print(c)

a = (np.sum(x) * np.sum(y) - n * np.sum(x * y)) / (np.sum(x) * np.sum(x) - n * np.sum(x * x))
b = (np.sum(y) - a * np.sum(x)) / n

A = np.vstack([x, np.ones(len(x))]).T
a1, b1, = np.linalg.lstsq(A, y)[0]
print(a, b)
print(a1, b1)

xm = sum(x) / n
ym = sum(y) / n
coeff_corr = sum((x - xm) * (y - ym)) / np.sqrt(sum((x - xm)**2) * sum((y - ym)**2))
print('Coeff_corr = ', coeff_corr)
plt.plot([0, 1], [b, a + b])
#plt.show()
plt.savefig('task5.png')


