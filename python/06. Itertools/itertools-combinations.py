# https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations


S, k = input().split()
S = sorted(S)

for j in range(int(k)):
    print(*["".join(i) for i in combinations(S, j + 1)], sep="\n")
