from decimal import Decimal

import numpy as np
import matplotlib.pyplot as plt
import math

#окружность
x0 = 3
y0 = 8
r = 3
angle = np.linspace(0, 2 * np.pi, 1000)
x = r * np.cos(angle) + x0
y = r * np.sin(angle) + y0
plt.plot(x, y)

#эллипс
x0 = 1
y0 = -2
a = 8
b = 4
angle = np.linspace(0, 2*np.pi, 1000)
x1 = a * np.cos(angle) + x0
y1 = b * np.sin(angle) + y0
plt.plot(x1, y1)

#гипербола
x = []
y = []
y1 = []
xx1 = []
x_ = 0.
a = 0.3
b = 3
while x_ <= 10:
  x_ = x_ + 0.001
  if (x_**2/a**2 - 1) > 0:
    x.append(x_)
    xx1.append(((- 1) * x_))
    y1.append(math.sqrt((x_**2/a**2 - 1) / b**2))
    y.append(-math.sqrt((x_**2/a**2 - 1) / b**2))

    plt.plot(x, y1)
    plt.plot(x, y)
    plt.plot(xx1, y1)
    plt.plot(xx1, y)


plt.axis('scaled')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
#plt.show()
plt.savefig('task3_fig1.png')
