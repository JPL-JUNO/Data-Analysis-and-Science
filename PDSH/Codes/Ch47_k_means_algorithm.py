"""
@Description: k-means algorithm
@Author(s): Stephen CUI
@Time: 2023-04-18 14:10:38
"""

from sklearn.metrics import pairwise_distances_argmin
import matplotlib.pyplot as plt
import numpy as np
from numpy import ndarray
from sklearn.datasets import make_blobs
from typing import Tuple


def find_cluster(X: ndarray, n_clusters: int, rseed: int = 2) -> Tuple[ndarray, ndarray]:
    rng = np.random.RandomState(seed=rseed)
    i = rng.permutation(X.shape[0])[:n_clusters]
    centers = X[i]
    while True:
        labels = pairwise_distances_argmin(X, centers)
        new_centers = np.array([X[labels == i].mean(axis=0)
                               for i in range(n_clusters)])
        if np.all(centers == new_centers):
            break
        centers = new_centers
    return centers, labels


if __name__ == '__main__':
    X, y_true = make_blobs(n_samples=300, centers=4,
                           cluster_std=.6, random_state=0)
    centers, labels = find_cluster(X, 4)
    plt.scatter(X[:, 0], X[:, 1],
                c=labels, s=50)

    centers, labels = find_cluster(X, 4, rseed=0)
    fig = plt.figure()
    plt.scatter(X[:, 0], X[:, 1], c=labels, s=50)

    centers, labels = find_cluster(X, 6, rseed=0)
    fig = plt.figure()
    plt.scatter(X[:, 0], X[:, 1], c=labels, s=50)
