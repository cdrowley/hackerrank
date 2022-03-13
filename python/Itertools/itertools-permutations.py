# https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations

UI = input().split()

S = sorted(list(UI[0]))
k = int(UI[1])

for i in permutations(S, int(k)):
    print("".join(i))
