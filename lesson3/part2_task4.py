import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 5, 301)
#print(np.poly([1, 1, 2]))
plt.plot(x, np.exp(x) / x + (x-1) / x)
plt.plot(x, x**2 - 1)
#plt.plot(x, x**3 + np.exp(x) - 1)
# plt.plot(x,np.polyval([1., -4.,  5., -2.],x))
# plt.plot(x, np.exp(x))
plt.xlabel('x')
plt.ylabel('y')
#plt.xlim(-10, 30)
plt.axis('equal')
plt.ylim(-2, 30)
plt.grid(True)
plt.show()
print(np.roots([1., 0, -1.]))
a = -1
print(np.exp(a) / a + (a - 1) / a)

#exp(x) + x∙(1 – y) = 1 Решите систему уравнений:
#y = x2 – 1
