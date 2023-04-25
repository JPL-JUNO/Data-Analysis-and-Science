"""
@Description: Ensembles of Estimators: Random Forests
@Author: Stephen CUI
@Time: 2023-04-17 09:59:16
"""
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from Ch44 import visualize_classifier, X, y
import numpy as np
import matplotlib.pyplot as plt

tree = DecisionTreeClassifier()
bag = BaggingClassifier(tree, n_estimators=100,
                        max_samples=.8,
                        random_state=1)
bag.fit(X, y)
visualize_classifier(bag, X, y)


from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=0)
visualize_classifier(model, X, y)

rng = np.random.RandomState(42)
x = 10 * rng.rand(200)


def model(x, sigma=.3):
    fast_oscillation = np.sin(5 * x)
    slow_oscillation = np.sin(.5 * x)
    noise = sigma * rng.randn(len(x))

    return slow_oscillation + fast_oscillation + noise


y = model(x)
fig = plt.figure()
plt.errorbar(x, y, .3, fmt='o', alpha=.5)
# plt.plot(x, y, 'ko')

from sklearn.ensemble import RandomForestRegressor
forest = RandomForestRegressor(200)
forest.fit(x[:, None], y)
x_fit = np.linspace(0, 10, 1000)
y_fit = forest.predict(x_fit[:, None])
y_true = model(x_fit, sigma=0)
plt.plot(x_fit, y_fit, '-r')
plt.plot(x_fit, y_true, '-k', alpha=.5)
