# https://www.hackerrank.com/challenges/np-polynomials/problem

import numpy as np

a = list(map(float, input().split()))

print(np.polyval(a, int(input())))
