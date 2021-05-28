import numpy as np
import matplotlib.pyplot as plt

from pylab import *
from mpl_toolkits.mplot3d import Axes3D

# Две параллельные плоскости
fig = figure()
ax = Axes3D(fig)
X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)
X, Y = np.meshgrid(X, Y)
Z = -2*X - 15*Y
Z1 = -2*X - 15*Y + 220
ax.plot_wireframe(X, Y, Z)
ax.plot_surface(X, Y, Z1)
ax.scatter(0, 0, 0, 'z', 50, 'red')
plt.savefig('task4_graph1.png')


