import numpy as np
import matplotlib.pyplot as plt
from random import random

k = 1
x = np.linspace(0, 20, 121)
plt.plot(x, np.sin(x*k), marker='o')
plt.savefig(f'graph1 {k}.png')
print(k)

k = random()
x = np.linspace(0, 20, 121)
plt.plot(x, np.sin(x*k), marker='o')
plt.savefig(f'graph1 {round(k, 2)}.png')
print(k)

