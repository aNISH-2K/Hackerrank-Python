import numpy
m = numpy.array(input().split(), float)
n = float(input())
print(numpy.polyval(m, n))
