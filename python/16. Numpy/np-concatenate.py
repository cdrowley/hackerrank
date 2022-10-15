# https://www.hackerrank.com/challenges/np-concatenate/problem

import numpy

N, M, P = list(map(int, input().split()))

A = numpy.array([list(map(int, input().split())) for _ in range(N)])
B = numpy.array([list(map(int, input().split())) for _ in range(M)])

print(numpy.concatenate((A, B), axis=0))
