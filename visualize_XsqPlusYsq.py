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
Z = X**2+Y**2

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, color='grey',
        linewidth=0, antialiased=False, alpha = 0.5, zorder=0)

Z2 = 5*np.arange(0, 10, .25)

ax.plot_surface(2, Y ,Z2, color='green', linewidth=0, zorder=1, alpha=0.8)

y = np.arange(-5, 5, 0.25)
ax.plot([2]*len(y), y, 4+y**2 , lw=2, color='green', zorder=2)

z = np.arange(-1.01, 50, 0.25)
ax.plot([0]*len(z), [0]*len(z), z , lw=1, color='k', zorder=3)

ax.plot([0], [0], [0] , color='red', zorder=4)

y1 = np.arange(0,sqrt(16),0.2)
x1 = np.arange(0,2,2.0/len(y1))
z1 = [20]*len(y1)

ax.plot(x1, y1, z1 , lw=1, color='blue', zorder=5)

ax.plot(x1, -y1, z1 , lw=1, color='blue', zorder=5)

y1 = [0]*len(x1)
z1 = [4]*len(y1)
ax.plot(x1, y1, z1 , lw=1, color='blue', zorder=6)

ax.set_zlim(-1.01, 50.01)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

plt.show()
