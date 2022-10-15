# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem

import numpy

N, M = map(int, input().split())
matrix = numpy.array([list(map(int, input().split())) for _ in range(N)])
print(numpy.transpose(matrix))
print(matrix.flatten())
