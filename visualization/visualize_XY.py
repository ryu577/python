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

#Define the quadratic function.
Z = X*Y

#Plot the paraboloid
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, color='grey',
        linewidth=0, antialiased=False, alpha = 0.5, zorder=0)

Z2 = 5*np.arange(-5, 5, .25)

#We plot a plane perpendicular to the z-axis. So, x is always 2.
ax.plot_surface(Y, 2-Y ,Z2, color='green', linewidth=0, zorder=1, alpha=0.8)

#Now plot the quadratic curve that defines the intersection of the paraboloid and the plane.
y = np.arange(-5, 5, 0.25)
ax.plot(y, y, y*(2-y) , lw=2, color='green', zorder=2)

#Plot the z-axis
z = np.arange(-25, 25, 0.25)
ax.plot([0]*len(z), [0]*len(z), z , lw=1, color='k', zorder=3)

#Plot two vectors along the gradient of the paraboloid, intersecting the parabola of intersection.
y1 = np.arange(0,4,0.2)
x1 = np.arange(0,2,2.0/len(y1))
z1 = [20]*len(y1)
ax.plot(x1, y1, z1 , lw=1, color='blue', zorder=5)
ax.plot(x1, -y1, z1 , lw=1, color='blue', zorder=5)

#Plot a vector along the gradient of the paraboloid, intersecting the parabola of intersection at its minima.
y1 = [0]*len(x1)
z1 = [1]*len(y1)
ax.plot(x1, y1, z1 , lw=1, color='blue', zorder=6)

#Set axis limits etc and show.
ax.set_zlim(-25, 25)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

plt.show()

