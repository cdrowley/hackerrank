# https://www.hackerrank.com/challenges/py-collections-deque/problem

from collections import deque

N = int(input())
D = deque()

for _ in range(N):
    UI = input().split()
    if len(UI) == 1:
        eval("D.{}()".format(UI[0]))
    else:
        eval("D.{}({})".format(UI[0], UI[1]))

print(*D)
