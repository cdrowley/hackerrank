# https://www.hackerrank.com/challenges/re-start-re-end/problem

import re

S, P = input(), re.compile(input())
M = P.search(S)

if not M:
    print((-1, -1))
else:
    while M:
        print((M.start(), M.end() - 1))
        M = P.search(S, M.start() + 1)
