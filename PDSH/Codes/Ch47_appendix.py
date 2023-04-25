"""
@Description: Expectation-Maximization
@Author(s): Stephen CUI
@Time: 2023-04-18 14:49:41
"""

from sklearn.datasets import make_blobs
from sklearn.metrics import pairwise_distances_argmin
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import Axes
X, y_true = make_blobs(n_samples=300, centers=4,
                       cluster_std=.60, random_state=0)
rng = np.random.RandomState(seed=42)
centers = [0, 4] + rng.randn(4, 2)


def draw_points(ax, c, factor=1):
    ax.scatter(X[:, 0], X[:, 1], c=c, s=50 * factor, alpha=.3)


def draw_centers(ax, centers, factor=1, alpha=1):
    ax.scatter(centers[:, 0], centers[:, 1], c=np.arange(4),
               edgecolor='black',
               s=200 * factor, alpha=alpha)
    ax.scatter(centers[:, 0], centers[:, 1], c='black',
               s=50 * factor, alpha=alpha)


def make_ax(fig, gs) -> Axes:
    ax = fig.add_subplot(gs)
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())
    return ax


fig = plt.figure(figsize=(15, 4))
gs = plt.GridSpec(4, 15, left=.02, right=.98, bottom=.05,
                  top=.95, wspace=.2, hspace=.2)
ax0 = make_ax(fig, gs[:4, :4])
ax0.text(.98, .98, 'random initialization', transform=ax0.transAxes,
         ha='right', va='top', size=16)
draw_points(ax0, 'gray', factor=2)
draw_centers(ax0, centers, factor=2)

for i in range(3):
    ax1 = make_ax(fig, gs[:2, 4 + 2 * i:6 + 2 * i])
    ax2 = make_ax(fig, gs[2:, 5 + 2 * i:7 + 2 * i])
    y_pred = pairwise_distances_argmin(X, centers)
    draw_points(ax1, y_pred)
    draw_centers(ax1, centers)

    new_centers = np.array([X[y_pred == i].mean(axis=0) for i in range(4)])
    draw_points(ax2, y_pred)
    draw_centers(ax2, centers, alpha=.3)
    draw_centers(ax2, new_centers)
    for i in range(4):
        ax2.annotate('', new_centers[i], centers[i],
                     arrowprops=dict(arrowstyle='->', linewidth=1, color='black'))

    centers = new_centers
    ax1.text(.95, .95, 'E-Step', transform=ax1.transAxes,
             ha='right', va='top', size=14)
    ax2.text(.95, .95, 'M-Step', transform=ax2.transAxes,
             ha='right', va='top', size=14)

y_pred = pairwise_distances_argmin(X, centers)
axf = make_ax(fig, gs[:4, -4:])
draw_points(axf, y_pred, factor=2)
draw_centers(axf, centers, factor=2)
axf.text(.98, .98, 'Final Clustering', transform=axf.transAxes,
         ha='right', va='top', size=16)
