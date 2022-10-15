# https://www.hackerrank.com/challenges/np-shape-reshape/problem

import numpy

UI = numpy.array(list(map(int, input().split())), int)
print(numpy.reshape(UI, (3, 3)))
