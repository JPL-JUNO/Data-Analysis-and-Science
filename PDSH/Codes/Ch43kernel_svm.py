"""
@Description: Beyond Linear Boundaries: Kernel SVM
@Author: Stephen CUI
@Time: 2023-04-13 16:35:10
"""
from sklearn.datasets import make_circles
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from Ch43 import plot_svc_decision_function
import numpy as np

X, y = make_circles(100, factor=.1, noise=.1)
clf = SVC(kernel='linear').fit(X, y)
fig = plt.figure()
# plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')
# plot_svc_decision_function(clf, plot_support=False)

r = np.exp(-(X ** 2).sum(1))

from mpl_toolkits import mplot3d
ax = plt.subplot(projection='3d')
ax.scatter(X[:, 0], X[:, 1], r, c=y, s=50, cmap='autumn')
ax.view_init(elev=20, azim=30)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('r')


clf = SVC(kernel='rbf', C=1e6)
clf.fit(X, y)

fig = plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')
plot_svc_decision_function(clf)
plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1],
            s=300, lw=1, facecolors='none')
