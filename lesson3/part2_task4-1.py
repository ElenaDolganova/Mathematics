import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt


x = np.linspace(-2, 7, 201)
plt.plot(x, (np.exp(x) + x - 1) / x)
plt.plot(x, x ** 2 - 1)
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-2, 25)
plt.grid(True)
plt.savefig('part2_task4-1.png')


def equations(p):
    x, y = p
    return (x ** 2 - 1 - y, ((np.exp(x) + x - 1) / x) - y)

x1, y1 = fsolve(equations, (-2, 2))
print(x1, y1)

x1, y1 = fsolve(equations, (2, 5))
print(x1, y1)

x1, y1 = fsolve(equations, (4, 16))
print(x1, y1)
