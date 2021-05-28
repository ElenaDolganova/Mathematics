# Нарисуйте график функции: y(x) = k∙cos(x – a) + b для некоторых (2-3 различных) значений параметров k, a, b

import numpy as np
import matplotlib.pyplot as plt

plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

a = [1, 0.2, 12]
b = [1, 0.2, -12, 12]
k = [1, 0.2, -12, 12]
x = np.linspace(-2*np.pi, 3*np.pi, 201)
for ai in a:
    plt.plot(x, np.cos(x - ai))
    plt.savefig('part2_task1_a.png')

for bi in b:
    plt.plot(x, np.cos(x) + bi)
    plt.savefig('part2_task1_b.png')

for ki in k:
    plt.plot(x, (ki) * np.cos(x))
    plt.savefig('part2_task1_k.png')

plt.plot(x, (k[1] * np.cos(x - a[2]) + b[0]))
plt.plot(x, (k[2] * np.cos(x - a[1]) + b[2]))
plt.plot(x, (k[0] * np.cos(x - a[2]) + b[3]))
plt.savefig('part2_task1_abk.png')
