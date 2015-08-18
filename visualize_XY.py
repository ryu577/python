from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
Z = X*Y

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, color='grey',
        linewidth=0, antialiased=False, alpha = 0.5, zorder=0)

Z2 = 5*np.arange(0, 10, .25)

ax.plot_surface(X, Y, Z2, color='green',
	linewidth=0, zorder=1, alpha=0.8, zorder=1)

ax.set_zlim(-1.01, 50.01)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

plt.show()


