# https://www.hackerrank.com/challenges/np-eye-and-identity/problem

import numpy

numpy.set_printoptions(legacy="1.13")

N = tuple(map(int, input().split()))
print(numpy.eye(*N, k=0))
