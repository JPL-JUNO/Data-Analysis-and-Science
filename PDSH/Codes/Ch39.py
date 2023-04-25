"""
@Description: Hyperparameters and Model Validation
@Author: Stephen CUI
@Time: 2023-04-10 16:23:17
"""
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target

# Model Validation the Wrong Way
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=1)
model.fit(X, y)
y_model = model.predict(X)
from sklearn.metrics import accuracy_score
accuracy_score(y, y_model)


from sklearn.model_selection import train_test_split
X1, X2, y1, y2 = train_test_split(X, y, random_state=0,
                                  train_size=.5)
model.fit(X1, y1)
y2_model = model.predict(X2)
accuracy_score(y2, y2_model)

y2_model = model.fit(X1, y2).predict(X2)
y1_model = model.fit(X2, y2).predict(X1)
accuracy_score(y1, y1_model), accuracy_score(y2, y2_model)


from sklearn.model_selection import cross_val_score
cross_val_score(model, X, y, cv=5)

from sklearn.model_selection import LeaveOneOut
scores = cross_val_score(model, X, y, cv=LeaveOneOut())
scores.mean()


from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline


def PolynomialRegression(degree=2, **kwargs):
    return make_pipeline(PolynomialFeatures(degree=degree),
                         LinearRegression(**kwargs))


import numpy as np


def make_data(N, err=1.0, rseed=1):
    rng = np.random.RandomState(rseed)
    X = rng.rand(N, 1) ** 2
    y = 10 - 1. / (X.ravel() + .1)
    if err > 0:
        y += err * rng.randn(N)
    return X, y


X, y = make_data(40)

import matplotlib.pyplot as plt
plt.plot(X.ravel(), y, 'ko')

X_test = np.linspace(-.1, 1.1, 500)[:, np.newaxis]
axis = plt.axis()
for degree in (1, 3, 5):
    y_test = PolynomialRegression(degree).fit(X, y).predict(X_test)
    plt.plot(X_test.ravel(), y_test, label='degree={}'.format(degree))
plt.xlim(-.1, 1.0)
plt.ylim(-2, 12)
plt.legend()


from sklearn.model_selection import validation_curve
degree = np.arange(21)
train_score, val_score = validation_curve(
    PolynomialRegression(), X, y,
    param_name='polynomialfeatures__degree',
    param_range=degree, cv=7
)
fig = plt.figure()
plt.plot(degree, np.median(train_score, axis=1),
         color='blue', label='training_scores')
plt.plot(degree, np.median(val_score, axis=1),
         color='red', label='validation score')
plt.legend()
plt.ylim(0, 1)
plt.xlabel('degree')
plt.ylabel('score')


fig = plt.figure()
plt.plot(X.ravel(), y, 'ko')
lim = plt.axis()
y_test = PolynomialRegression(3).fit(X, y).predict(X_test)
plt.plot(X_test.ravel(), y_test)
plt.axis(lim)


X2, y2 = make_data(200)
fig = plt.figure()
plt.plot(X2.ravel(), y2, 'ko')
degree = np.arange(21)
train_score2, val_score2 = validation_curve(
    PolynomialRegression(), X2, y2,
    param_name='polynomialfeatures__degree',
    param_range=degree, cv=7
)
fig = plt.figure()
plt.plot(degree, np.median(train_score2, axis=1),
         color='blue', label='training_scores')
plt.plot(degree, np.median(val_score2, axis=1),
         color='red', label='validation score')
plt.plot(degree, np.median(train_score, axis=1),
         color='blue', label='training_scores', linestyle='dashed')
plt.plot(degree, np.median(val_score, axis=1),
         color='red', label='validation score', linestyle='dashed')
plt.legend()
plt.ylim(0, 1)
plt.xlabel('degree')
plt.ylabel('score')


from sklearn.model_selection import learning_curve
fig, ax = plt.subplots(1, 2, figsize=(16, 6))
fig.subplots_adjust(left=.0625, right=.95, wspace=.1)

for i, degree in enumerate((2, 9)):
    N, train_lc, val_lc = learning_curve(
        PolynomialRegression(degree), X, y, cv=7,
        train_sizes=np.linspace(.3, 1, 25)
    )
    ax[i].plot(N, np.mean(train_lc, axis=1),
               color='blue', label='training score')
    ax[i].plot(N, np.mean(val_lc, axis=1),
               color='red', label='validation score')
    ax[i].hlines(np.mean([train_lc[-1], val_lc[-1]]), N[0],
                 N[-1], color='gray', linestyle='dashed')
    ax[i].set_ylim(0, 1)
    ax[i].set_xlim(N[0], N[-1])
    ax[i].set_xlabel('training size')
    ax[i].set_ylabel('score')
    ax[i].set_title('degree = {}'.format(degree), size=14)
    ax[i].legend()


from sklearn.model_selection import GridSearchCV

param_grid = {'polynomialfeatures__degree': np.arange(21),
              'linearregression__fit_intercept': [True, False]}
grid = GridSearchCV(PolynomialRegression(), param_grid=param_grid, cv=7)
grid.fit(X, y)


model = grid.best_estimator_
grid.best_params_

fig = plt.figure()
plt.plot(X.ravel(), y, 'ko')
lim = plt.axis()
y_test = model.fit(X, y).predict(X_test)
plt.plot(X_test.ravel(), y_test)
