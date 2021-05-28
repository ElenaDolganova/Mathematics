from pylab import *
from mpl_toolkits.mplot3d import Axes3D

# Гиперболический параболоид
fig = figure()
ax = Axes3D(fig)
X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)
X, Y = np.meshgrid(X, Y)
Z = X**2 - Y**2
ax.plot_wireframe(X, Y, Z)
ax.scatter(0, 0, 0, 'z', 50, 'red')
plt.savefig('task4_graph2.png')
