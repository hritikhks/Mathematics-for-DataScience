from scipy.spatial import ConvexHull as hull
from random import random as rd
from matplotlib import pyplot as plt

Xs = [round(rd()*10-5,1) for _ in range(24)]
Ys = [round(rd()*10-5,1) for _ in range(24)]
H = hull([(Xs[i],Ys[i]) for i in range(24)])
plt.scatter(Xs, Ys, color = 'g')
plt.plot([Xs[i] for i in H.vertices], [Ys[i] for i in H.vertices], color = 'b')
plt.plot([Xs[H.vertices[-1]],Xs[H.vertices[0]]], [Ys[H.vertices[-1]],Ys[H.vertices[0]]], color = 'b')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Convex Hull')
plt.show()
