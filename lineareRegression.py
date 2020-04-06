import numpy as np
import matplotlib.pyplot as plt
import pandas
from data import *

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

x, y = regression_data()
print(x.shape)
x = x.reshape(-1, 1)
print(x.shape)
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state = 42)


regr = LinearRegression()
regr.fit(x_train, y_train) #Training
print (regr.score(x_test, y_test)) #Testing
y_pred = regr.predict(x_test)
errorMAE = mean_absolute_error(y_test, y_pred)
errorMSE = mean_squared_error(y_test, y_pred, squared=False)
print(errorMAE)
print(errorMSE)

plt.scatter(x, y)
plt.plot(x_test, y_pred)
plt.show()