# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations_with_replacement

S, k = input().split()

print(
    *["".join(i) for i in list(combinations_with_replacement(sorted(S), int(k)))],
    sep="\n"
)
