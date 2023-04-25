"""
@Description: Gaussian Naive Bayes Example
@Author: Stephen CUI
@Time: 2023-04-11 15:35:52
"""
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np

X, y = make_blobs(100, 2, centers=2, random_state=2, cluster_std=1.5)
fig, ax = plt.subplots()

ax.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='RdBu')
ax.set_title('Naive Bayes Model', size=14)

xlim = (-8, 8)
ylim = (-15, 5)

xg = np.linspace(xlim[0], xlim[1], 60)
yg = np.linspace(ylim[0], ylim[1], 40)
xx, yy = np.meshgrid(xg, yg)
Xgrid = np.vstack([xx.ravel(), yy.ravel()]).T

for label, color in enumerate(['red', 'blue']):
    mask = (y == label)
    mu, std = X[mask].mean(axis=0), X[mask].std(axis=0)
    P = np.exp(-.5 * (Xgrid - mu) ** 2 / std ** 2).prod(axis=1)
    Pm = np.ma.masked_array(P, P < .03)
    ax.pcolorfast(xg, yg, Pm.reshape(xx.shape), alpha=.5,
                  cmap=color.title() + 's')
    # 画等高线
    ax.contour(xx, yy, P.reshape(xx.shape),
               levels=[.01, .2, .5, .9],  # 我不能确定这里的数值画的是正确的概率
               colors=color, alpha=.2)
ax.set(xlim=xlim, ylim=ylim)
