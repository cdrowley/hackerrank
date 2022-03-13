# https://www.hackerrank.com/challenges/np-min-and-max/problem

import numpy as np

N, M = map(int, input().split())
A = np.array([input().split() for M in range(N)], int)
print(np.max(np.min(A, axis=1)))
