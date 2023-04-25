"""
@Description: Motivating Gaussian Mixtures: Weakness of k-Means
@Author(s): Stephen CUI
@Time: 2023-04-19 11:28:23
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

X, y_true = make_blobs(n_samples=400, centers=4,
                       cluster_std=.6, random_state=0)
X = X[:, ::-1]
kmeans = KMeans(4, random_state=0, n_init='auto')
labels = kmeans.fit(X).predict(X)
plt.scatter(X[:, 0], X[:, 1], c=labels, s=40)


def plot_kmeans(kmeans, X, ax=None):
    labels = kmeans.fit_predict(X)
    ax = ax or plt.gca()
    ax.scatter(X[:, 0], X[:, 1], c=labels, s=40, zorder=2)
    centers = kmeans.cluster_centers_
    radii = [cdist(X[labels == i], [center]).max()
             for i, center in enumerate(centers)]
    for c, r in zip(centers, radii):
        ax.add_patch(plt.Circle(c, r, ec='black', fc='lightgray',
                                lw=3, zorder=1, alpha=.7))
    ax.grid(True)
    ax.axis('equal')


kmeans = KMeans(n_clusters=4, n_init='auto', random_state=0)

plot_kmeans(kmeans, X)
plt.savefig('../Figures/fig48-2.png', dpi=300)


rng = np.random.RandomState(13)
X_stretched = np.dot(X, rng.randn(2, 2))
kmeans = KMeans(n_clusters=4, n_init='auto', random_state=0)
fig = plt.figure()
plot_kmeans(kmeans, X_stretched)
plt.savefig('../Figures/fig48-3.png', dpi=300)
