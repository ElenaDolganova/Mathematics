import numpy as np
import matplotlib.pyplot as plt

from pylab import *
from mpl_toolkits.mplot3d import Axes3D


# Однополостной гиперболоид
fig = figure()
ax = Axes3D(fig)
X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)
X, Y = np.meshgrid(X, Y)

Z = np.sqrt(0.1*X**2 + 20*Y**2 + 5)
ax.plot_wireframe(X, Y, Z)
ax.scatter(0, 0, 0, 'z', 50, 'red')
plt.savefig('task4_graph3.png')

