# https://www.hackerrank.com/challenges/np-linear-algebra/problem

import numpy as np

N = int(input())
A = np.array([input().split() for _ in range(N)], float)
print(round(np.linalg.det(A), 2))
