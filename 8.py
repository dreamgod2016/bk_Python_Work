import numpy
import matplotlib.pyplot as plt

x = numpy.arange(-5,5,0.1)
y = x ** 3
plt.title("y = x **3")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y)
plt.show()