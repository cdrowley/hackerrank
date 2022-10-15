# https://www.hackerrank.com/challenges/compress-the-string/problem

from itertools import groupby


for k, g in groupby(input()):
    print(f"({len(list(g))}, {k})", end=" ")
