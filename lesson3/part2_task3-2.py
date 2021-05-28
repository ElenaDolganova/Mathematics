import numpy as np
import matplotlib.pyplot as plt
import math

#окружность в полярных координатах

x0 = 4
y0 = 4
r = 4
alpha = np.linspace(0, 2 * np.pi, 200)
x = r * np.cos(alpha) + x0
y = r * np.sin(alpha) + y0
plt.polar(x, y)
plt.grid(True)
plt.savefig('part2_task3-2.png')


