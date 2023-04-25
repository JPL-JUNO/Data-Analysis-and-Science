"""
@Description: k-Means for Color Compression
@Author(s): Stephen CUI
@Time: 2023-04-19 10:32:12
"""
import PIL
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_sample_image
china = load_sample_image('china.jpg')
ax = plt.axes(xticks=[], yticks=[])
ax.imshow(china)

assert china.shape == (427, 640, 3)

data = china / 255
data = data.reshape(-1, 3)
assert data.shape == (273280, 3)


def plot_pixels(data, title, colors=None, N: int = 10_000):
    if colors is None:
        colors = data
    rng = np.random.RandomState(0)
    i = rng.permutation(data.shape[0])[:N]
    colors = colors[i]
    R, G, B = data[i].T

    fig, ax = plt.subplots(1, 2, figsize=(16, 6))
    ax[0].scatter(R, G, color=colors, marker='.')
    ax[0].set(xlabel='red', ylabel='green', xlim=(0, 1), ylim=(0, 1))

    ax[1].scatter(R, B, color=colors, marker='.')
    ax[1].set(xlabel='red', ylabel='blue', xlim=(0, 1), ylim=(0, 1))

    fig.suptitle(title)


plot_pixels(data, title='Input color space: 16 million possible colors')

from sklearn.cluster import MiniBatchKMeans
kmeans = MiniBatchKMeans(16, n_init='auto')
kmeans.fit(data)
new_colors = kmeans.cluster_centers_[kmeans.predict(data)]

plot_pixels(data, colors=new_colors, title='Reduced color space: 16 colors')

china_recolored = new_colors.reshape(china.shape)
fig, ax = plt.subplots(1, 2, figsize=(16, 6),
                       subplot_kw=dict(xticks=[], yticks=[]))
fig.subplots_adjust(wspace=.05)
ax[0].imshow(china)
ax[0].set_title('Original Image', size=16)
# 不再那么连续顺滑
ax[1].imshow(china_recolored)
ax[1].set_title('16-color Image', size=16)
