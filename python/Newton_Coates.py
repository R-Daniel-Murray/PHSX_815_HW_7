import scipy
from matplotlib import pyplot as plt
import numpy as np

###construct a polynomial. These could be inputs instead of fixed
x = np.linspace(-5, 5, 1000)
coeffs_ = [3, 4, -25, 120, 1]
p = np.poly1d(coeffs_)


t = len(x)
integral = 0
for i in range (t-1):
    y = p(x[i])
    y_av = (p(x[i])+p(x[i+1]))/2
    # print(y_av)
    integral += y_av * 0.01
    # y_av = (y([i]+y[i-1])/2)

print (integral)

### If you want to look at the graph you can do so
# plt.plot(x, p(x))
# plt.show()