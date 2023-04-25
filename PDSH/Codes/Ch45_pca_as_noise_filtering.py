"""
@Description: PCA as noise filtering
@Author: Stephen CUI
@Time: 2023-04-17 15:33:25
"""
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
import numpy as np


def plot_digits(data):
    fig, axes = plt.subplots(4, 10, figsize=(10, 4),
                             subplot_kw={'xticks': [], 'yticks': []},
                             gridspec_kw=dict(hspace=.1, wspace=.1))
    for i, ax in enumerate(axes.flat):
        ax.imshow(data[i].reshape(8, 8),
                  cmap='binary', interpolation='nearest',
                  clim=(0, 16))


digits = load_digits()
plot_digits(digits.data)
rng = np.random.default_rng(seed=42)
rng.normal(10, 2)
# 以 digits.data 中的每个数据点为均值，scale 为 4，生成正态分布的数据，用了广播机制
noisy = rng.normal(digits.data, 4)
plot_digits(noisy)

pca = PCA(.50).fit(noisy)
pca.n_components_

components = pca.transform(noisy)
filtered = pca.inverse_transform(components)
plot_digits(filtered)
