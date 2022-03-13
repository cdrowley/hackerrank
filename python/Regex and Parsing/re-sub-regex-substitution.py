# https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem

import re

PATTERN = r"(?<= )(&&|\|\|)(?= )"
N = int(input())

for _ in range(N):
    func = lambda x: "and" if x.group() == "&&" else "or"
    result = re.sub(PATTERN, func, input())
    print(result)
