from numpy import array
from numpy.linalg import inv
from matplotlib import pyplot

data = array([
	[0.05, 0.12],
	[0.18, 0.22],
	[0.31, 0.35],
	[0.42, 0.38],
	[0.5, 0.49],
	])
X, y = data[:,0], data[:,1]
X = X.reshape((len(X), 1))

pyplot.scatter(X, y)
pyplot.show()

# linear least squares
b = inv(X.T.dot(X)).dot(X.T).dot(y)
print("Direct inverses",b)

# let b = [b1, b2]
# predict using coefficients
yhat = X.dot(b)
print("yhat", yhat)
# plot data and predictions
pyplot.scatter(X, y)
pyplot.plot(X, yhat, color='red')
pyplot.show()