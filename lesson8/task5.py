from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def Q(x, y, z):
  return (x**2 + y**2 + z**2)


A = np.array([[1, 2, -1], [8, -5, 2]])
B = np.array([[1, 12]])

# y = 10x - 14
# z = 21x - 29

fig = figure()
ax = Axes3D(fig)
X = np.arange(-50, 50, 1)
Y = np.arange(-50, 50, 1)
X, Y = np.meshgrid(X, Y)
ax.plot_surface(X, Y, Q(X, 10*X - 14, 21*X - 29))
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

BT = np.transpose(B)
xyz = np.linalg.lstsq(A, BT)
print('Нормальное псевдорешение недоопределенной системы уравнений:')
print(xyz)
