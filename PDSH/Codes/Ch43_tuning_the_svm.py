"""
@Description: Tuning the SVM: Softening Margins
@Author: Stephen CUI
@Time: 2023-04-13 17:30:55
"""

from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from Ch43 import plot_svc_decision_function

X, y = make_blobs(n_samples=100, centers=2,
                  random_state=0, cluster_std=1.2)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')

fig, ax = plt.subplots(1, 2, figsize=(16, 6))
fig.subplots_adjust(left=.0625, right=.95, wspace=.1)
for axi, C in zip(ax, [10, .1]):
    model = SVC(kernel='linear', C=C).fit(X, y)
    axi.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')
    plot_svc_decision_function(model, axi)
    axi.scatter(model.support_vectors_[:, 0],
                model.support_vectors_[:, 1], s=300, lw=1, facecolors='none')
    axi.set_title('C = {}'.format(C), size=14)
