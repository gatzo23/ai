import numpy as np
import matplotlib.pyplot as plt

def e_function(a, b):
    c = range(a,b)
    c_np = np.array(c, dtype=np.int8)
    eFkt = np.exp(c_np)    
    plt.plot(range(a,b), eFkt, color='blue')
    plt.show()

a = 1
b = 5
e_function(a,b)
