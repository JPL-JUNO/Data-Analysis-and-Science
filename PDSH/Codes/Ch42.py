"""
@Description: In Depth: Linear Regression
@Author: Stephen CUI
@Time: 2023-04-11 17:48:46
"""


import matplotlib.pyplot as plt
import numpy as np


rng = np.random.RandomState(1)
x = 10 * rng.rand(50)
y = 2 * x - 5 + rng.randn(50)
plt.plot(x, y, 'ko')
from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=True)
model.fit(x[:, np.newaxis], y)
xfit = np.linspace(0, 10, 1000)
yfit = model.predict(xfit[:, np.newaxis])
plt.plot(xfit, yfit)
print('Model slope: {}'.format(model.coef_))
print('Model intercept: {}'.format(model.intercept_))


X = 10 * rng.rand(100, 3)
y = .5 + np.dot(X, [1.5, -2, 1.])
model.fit(X, y)
print('Model intercept: {}'.format(model.intercept_))
print('Model coefficient: {}'.format(model.coef_))


from sklearn.preprocessing import PolynomialFeatures
x = np.array([2, 3, 4])
poly = PolynomialFeatures(3, include_bias=False)
poly.fit_transform(x[:, None])  # 将一维的 x 转为 二维


from sklearn.pipeline import make_pipeline
poly_model = make_pipeline(PolynomialFeatures(7),
                           LinearRegression())
x = 10 * rng.rand(50)
y = np.sin(x) + .1 * rng.randn(50)
poly_model.fit(x[:, np.newaxis], y)
yfit = poly_model.predict(xfit[:, np.newaxis])

fig = plt.figure()
plt.plot(x, y, 'ko')
plt.plot(xfit, yfit)

from Ch42appendix import GaussianFeatures

gauss_model = make_pipeline(GaussianFeatures(20), LinearRegression())
gauss_model.fit(x[:, np.newaxis], y)
yfit = gauss_model.predict(xfit[:, np.newaxis])

fig = plt.figure()

plt.plot(x, y, 'ko')
plt.plot(xfit, yfit)
plt.xlim(0, 10)


def basic_plot(model, title=None):
    fig, ax = plt.subplots(2, sharex=True)
    model.fit(x[:, np.newaxis], y)
    ax[0].scatter(x, y)
    ax[0].plot(xfit, model.predict(xfit[:, np.newaxis]))
    ax[0].set(xlabel='x', ylabel='y', ylim=(-1.5, 1.5))
    if title:
        ax[0].set_title(title)
    ax[1].plot(model.steps[0][1].centers_,
               model.steps[1][1].coef_)
    ax[1].set(xlabel='basis location', ylabel='coefficient', xlim=(0, 10))


model = make_pipeline(GaussianFeatures(30), LinearRegression())
basic_plot(model)


from sklearn.linear_model import Ridge
model = make_pipeline(GaussianFeatures(30), Ridge(alpha=.1))
basic_plot(model, title='Ridge Regression')


from sklearn.linear_model import Lasso
model = make_pipeline(GaussianFeatures(30), Lasso(alpha=.001, max_iter=2000))
basic_plot(model, title='Lasso Regression')
