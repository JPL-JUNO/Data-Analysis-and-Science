"""
@Description: In Depth: Decision Trees and Random Forests
@Author: Stephen CUI
@Time: 2023-04-16 21:33:09
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.tree import DecisionTreeClassifier
from numpy import ndarray
from matplotlib.pyplot import Axes
plt.style.use('ggplot')

X, y = make_blobs(n_samples=300, centers=4,
                  random_state=0, cluster_std=1.0)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='rainbow')
tree = DecisionTreeClassifier().fit(X, y)


def visualize_classifier(model: object, X: ndarray, y: ndarray,
                         ax: Axes = None,
                         cmap: str = 'rainbow') -> None:
    assert X.ndim == 2, 'X must be 2-dimensional'
    ax = ax or plt.gca()
    ax.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=cmap,
               clim=(y.min(), y.max()), zorder=3)
    ax.axis('tight')
    ax.axis('off')
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    model.fit(X, y)
    xx, yy = np.meshgrid(np.linspace(*xlim, num=200),
                         np.linspace(*ylim, num=200))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

    _ = ax.contourf(xx, yy, Z, alpha=0.3,
                    cmap=cmap,
                    zorder=1)
    ax.set(xlim=xlim, ylim=ylim)


if __name__ == '__main__':
    visualize_classifier(DecisionTreeClassifier(), X, y)
