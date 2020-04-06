import numpy as np
import matplotlib.pyplot as plt
import pandas

np.random.seed(42)

def f(x):
    return 2.0 * x + 5.0

def classification_data():
    x1 = np.random.multivariate_normal(mean=[5.0, 5.0], cov=[[1,0], [0,1]], size=15)
    y1 = np.array([0 for i in range(15)])
    x2 = np.random.multivariate_normal(mean=[-5.0, -5.0], cov=[[1,0], [0,1]], size=15)
    y2 = np.array([1 for i in range(15)])
    x = np.concatenate((x1,x2))
    y = np.concatenate((y1,y2))
    return x, y


def regression_data():
    x = np.random.uniform(low=-10.0, high=10.0, size=100)
    y = f(x) + np.random.normal(scale=20.0, size=100)
    return x, y

# x, y = regression_data()
# plt.scatter(x, y)
# plt.show()

# colors = np.array(["red","blue"])
# x, y = classification_data()
# print(x.shape, y.shape)
# plt.scatter(x[:,0], x[:,1], c=colors[y[:]])
# plt.show()
