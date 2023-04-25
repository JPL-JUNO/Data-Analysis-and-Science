"""
@Description: Introducing k-Means
@Author(s): Stephen CUI
@Time: 2023-04-18 11:31:02
"""
from sklearn.datasets import make_blobs, make_moons
from sklearn.cluster import KMeans
import numpy as np
from sklearn.cluster import SpectralClustering
import matplotlib.pyplot as plt
plt.style.use('ggplot')

if __name__ == '__main__':

    X, y_true = make_blobs(n_samples=300, centers=4,
                           cluster_std=.6, random_state=0)
    plt.scatter(X[:, 0], X[:, 1], s=50)

    kmeans = KMeans(n_clusters=4, n_init='auto')
    kmeans.fit(X)
    y_kmeans = kmeans.predict(X)
    fig = plt.figure()
    centers = kmeans.cluster_centers_
    plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50)
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=150)
    X, y = make_moons(200, noise=.05, random_state=0)
    fig = plt.figure()
    labels = KMeans(2, random_state=0, n_init='auto').fit_predict(X)
    plt.scatter(X[:, 0], X[:, 1], c=labels,
                s=50)
    model = SpectralClustering(n_clusters=2,
                               affinity='nearest_neighbors',
                               assign_labels='kmeans')
    labels = model.fit_predict(X)
    fig = plt.figure()
    plt.scatter(X[:, 0], X[:, 1], c=labels,
                s=50)
