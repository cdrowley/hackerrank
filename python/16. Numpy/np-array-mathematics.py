# https://www.hackerrank.com/challenges/np-array-mathematics/problem

import numpy as np

N, M = list(map(int, input().split()))
A = np.array([input().split() for i in range(N)], dtype=np.int)
B = np.array([input().split() for i in range(N)], dtype=np.int)

for operator in "+ - * // % **".split():
    print(eval(f"A{operator}B"))
