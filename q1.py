from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
Z = (X**2 - Y**2)

surf = ax.plot_surface(X, Y, Z, linewidth=0, antialiased=False)

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-25, 25)
ax.xaxis.set_major_locator(LinearLocator(5))
ax.yaxis.set_major_locator(LinearLocator(5))
ax.zaxis.set_major_locator(LinearLocator(5))
ax.set_xlabel('x', fontsize=15)
ax.set_ylabel('y', fontsize=15)
ax.set_zlabel('(x^2 - y^2)', fontsize=15)    
fig.suptitle('f(x,y) = x^2 - y^2')

fig2 = plt.figure()
CS = plt.contour(X, Y, Z, 20)
labels = [(r-5)*abs(r-5) for r in range(11)]   
for i in range(len(labels)):
    CS.collections[i].set_label(labels[i])

plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.xlabel('x', fontsize=15)
plt.ylabel('y', fontsize=15)
plt.legend() 
fig2.suptitle('f(x,y) = x^2 - y^2')
plt.show()
