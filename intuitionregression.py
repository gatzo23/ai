import numpy as np
import matplotlib.pyplot as plt
import pandas
from data import *

x, y = regression_data()

m = 2
b = 5
y_pred = [m * xi + b for xi in x]

plt.scatter(x, y)
plt.plot(x, y_pred)
plt.show()