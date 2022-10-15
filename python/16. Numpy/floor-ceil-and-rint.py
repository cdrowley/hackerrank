# https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem

import numpy as np

np.set_printoptions(legacy="1.13")

A = np.array(list(map(float, input().split())))
[print(f(A)) for f in (np.floor, np.ceil, np.rint)]
