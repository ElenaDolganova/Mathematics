import numpy as np
import matplotlib.pyplot as plt
import math

#отрезок в полярных координатах

k = 2
b = 3
xx = np.linspace(1, 3, 100)
yy = k * xx + b
plt.polar(xx, yy)
plt.grid(True)
plt.savefig('part2_task3-3.png')

