"""
@Description: Introducing Principal Component Analysis
@Author: Stephen CUI
@Time: 2023-04-17 10:44:50
"""

import numpy as np
from numpy import ndarray
import matplotlib.pyplot as plt
from matplotlib.pyplot import Axes
plt.style.use('ggplot')

rng = np.random.RandomState(1)
X = np.dot(rng.rand(2, 2), rng.randn(2, 200)).T
plt.scatter(X[:, 0], X[:, 1])
plt.axis('equal')
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(X)

print(pca.components_)
print(pca.explained_variance_)


def draw_vector(v0: ndarray, v1: ndarray, ax: Axes = None):
    ax = ax or plt.gca()

    arrowprops = dict(arrowstyle='->',
                      linewidth=2,
                      color='black',
                      shrinkA=0, shrinkB=0)
    ax.annotate('', v1, v0, arrowprops=arrowprops)


fig = plt.figure()
plt.scatter(X[:, 0], X[:, 1], alpha=.5)
for length, vector in zip(pca.explained_variance_, pca.components_):
    v = vector * 3 * np.sqrt(length)
    # pca.mean_表示每个特征的均值，与X.mean(axis=0)计算结果相同
    draw_vector(pca.mean_, pca.mean_ + v)
plt.axis('equal')


pca = PCA(n_components=1)
pca.fit(X)
X_pca = pca.transform(X)
print('Original shape:', X.shape)
print('Transformed shape:', X_pca.shape)

fig = plt.figure()
X_new = pca.inverse_transform(X_pca)
plt.scatter(X[:, 0], X[:, 1], alpha=.2)
plt.scatter(X_new[:, 0], X_new[:, 1], s=2, alpha=.8)
plt.axis('equal')


from sklearn.datasets import load_digits
digits = load_digits()
digits.data.shape

pca = PCA(n_components=2)
projected = pca.fit_transform(digits.data)
print(digits.data.shape)
print(projected.shape)


plt.scatter(projected[:, 0], projected[:, 1],
            c=digits.target, edgecolor='none',
            alpha=.5, cmap='rainbow')
plt.xlabel('component 1')
plt.ylabel('component 2')
plt.colorbar()


pca = PCA().fit(digits.data)
plt.figure()
plt.plot(np.cumsum(pca.explained_variance_ratio_))
