"""
@Description: Introducing Scikit-Learn
@Author: Stephen CUI
@Time: 2023-04-10 11:24:53
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

iris = sns.load_dataset('iris')
iris.sample(5)

# sns.pairplot(iris, hue='species', height=1.5)

X_iris = iris.drop('species', axis=1)
y_iris = iris['species']

rng = np.random.RandomState(seed=42)
x = 10 * rng.rand(50)
y = 2 * x - 1 + rng.rand(50)
plt.plot(x, y, 'o')

from sklearn.linear_model import LinearRegression

model = LinearRegression(fit_intercept=True)

X = x[:, np.newaxis]

model.fit(X, y)

print(model.coef_, model.intercept_)

xfit = np.linspace(-1, 11)
Xfit = xfit[:, np.newaxis]
yfit = model.predict(Xfit)


plt.plot(x, y, 'o')
plt.plot(xfit, yfit)
