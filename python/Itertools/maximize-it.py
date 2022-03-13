# https://www.hackerrank.com/challenges/maximize-it/problem

from itertools import product

K, M = map(int, input().split())
n = [map(int, input().split()[1:]) for _ in range(K)]

prods = list(map(lambda x: sum(i * i for i in x) % M, product(*n)))
print(max(prods))
