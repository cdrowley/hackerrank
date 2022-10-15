# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem

import numpy

N = tuple(map(int, input().split()))

print(numpy.zeros(N, dtype=numpy.int))
print(numpy.ones(N, dtype=numpy.int))
