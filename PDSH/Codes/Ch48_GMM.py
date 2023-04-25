"""
@Description: Generalizing E-M: Gaussian Mixture Models
@Author(s): Stephen CUI
@Time: 2023-04-19 15:38:55
"""

from sklearn.mixture import GaussianMixture
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np
from numpy import ndarray
from matplotlib.pyplot import Axes
from matplotlib.patches import Ellipse


def draw_ellipse(position, covariance, ax=None, **kwargs):
    ax = ax or plt.gca()

    if covariance.shape == (2, 2):
        U, s, Vt = np.linalg.svd(covariance)
        width, height = 2 * np.sqrt(s)
        angle = np.degrees(np.arctan2(U[1, 0], U[0, 0]))
    elif isinstance(covariance, float):
        width = height = 2 * np.sqrt(covariance)
        angle = 0
    else:
        width, height = 2 * np.sqrt(covariance)
        angle = 0
    for nsig in range(1, 4):
        ax.add_patch(Ellipse(position, nsig * width, nsig * height,
                             angle=angle,
                             **kwargs))


def plot_gmm(gmm: object, X: ndarray, label: bool = True, ax: Axes = None):
    ax = ax or plt.gca()
    labels = gmm.fit(X).predict(X)

    if label:
        ax.scatter(X[:, 0], X[:, 1], c=labels, s=40, zorder=2)
    else:
        ax.scatter(X[:, 0], X[:, 1], s=40, zorder=2)
    ax.axis('equal')

    w_factor = .2 / gmm.weights_.max()
    for pos, covar, w in zip(gmm.means_, gmm.covariances_, gmm.weights_):
        draw_ellipse(pos, covar, alpha=w * w_factor)


if __name__ == '__main__':
    X, y_true = make_blobs(n_samples=400, centers=4,
                           cluster_std=.6, random_state=0)
    X = X[:, ::-1]
    gmm = GaussianMixture(n_components=4).fit(X)
    labels = gmm.predict(X)
    plt.scatter(X[:, 0], X[:, 1], c=labels, s=40)

    probs = gmm.predict_proba(X)
    probs[:5].round(3)

    fig = plt.figure()
    size = 50 * probs.max(axis=1) ** 2
    plt.scatter(X[:, 0], X[:, 1], c=labels, s=size)

    fig = plt.figure()
    gmm = GaussianMixture(n_components=4, random_state=42)
    plot_gmm(gmm, X)

    rng = np.random.RandomState(13)
    X_stretched = np.dot(X, rng.randn(2, 2))

    fig = plt.figure()
    gmm = GaussianMixture(n_components=4, random_state=42,
                          covariance_type='full')
    plot_gmm(gmm, X_stretched)

    # Gaussian Mixture Models as Density Estimation
    from sklearn.datasets import make_moons
    X_moon, y_moon = make_moons(n_samples=200, noise=.05, random_state=0)
    fig = plt.figure()
    plt.scatter(X_moon[:, 0], X_moon[:, 1])
    gmm2 = GaussianMixture(
        n_components=2, random_state=0, covariance_type='full')
    plot_gmm(gmm2, X_moon)

    fig = plt.figure()
    gmm16 = GaussianMixture(
        n_components=16, random_state=0, covariance_type='full')
    plot_gmm(gmm16, X_moon)

    X_new, y_new = gmm16.sample(400)
    fig = plt.figure()
    plt.scatter(X_new[:, 0], X_new[:, 1])
