from math import sqrt as sqrt
from numpy import arange as arange
import matplotlib.pyplot as plt
print('Ax^2 + Bx + C')
a = input('Enter the value of A: ')
b = input('Enter the value of B: ')
c = input('Enter the value of C: ')

a = float(a)
b = float(b)
c = float(c)

d = (b ** 2) - (4 * a * c)
d = float(d)

if d < 0:
    print('There are no real solutions.')
elif d == 0:
    x = ((-b) - sqrt((b ** 2) - (4 * a * c))) / (2 * a)
    print('There is one true solution: ')
else:
    x1 = ((-b) - sqrt((b ** 2) - (4 * a * c))) / (2 * a)
    x2 = ((-b) + sqrt((b ** 2) - (4 * a * c))) / (2 * a)
    print('There are two real solutions: ', x1, ' and ', x2)

xvals = arange(-50,50,2)

yvals = (a * (xvals ** 2)) + (b * xvals + (c))
plt.plot(xvals, yvals)
plt.grid(True)
plt.show()
