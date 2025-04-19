# Simple Machine Learning example
from sklearn.linear_model import LinearRegression
X = [[0], [1], [2]]
y = [0, 1, 2]
model = LinearRegression().fit(X, y)
print("ML model score:", model.score(X, y))
