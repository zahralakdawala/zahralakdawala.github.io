import statsmodels.api as sm
import pandas_datareader as web
import datetime

start = datetime.datetime(2019, 1, 1)
end = datetime.datetime(2020, 1, 1)
df = web.DataReader(['AAPL', 'IBM'], 'yahoo', start, end)['Adj Close']

X = df["IBM"] #X usually means our input variables (predictor)
y = df["AAPL"] #Y usually means our output/response variable

model = sm.OLS(y,X).fit()
# make the predictions using model
predictions = model.predict(X) #predictions are beta-slopes
print(model.summary())

#let'S add an intercept (beta_0) to our model
X= sm.add_constant(X)
model = sm.OLS(y, X).fit()
predictions = model.predict(X)
print(predictions[0:5])
print(model.summary())

from sklearn import linear_model
lm = linear_model.LinearRegression()
model = lm.fit(X, y)
predictions = lm.predict(X)
print(predictions[0:5])
print("Variance", lm.score(X, y))
print(lm.intercept_)

