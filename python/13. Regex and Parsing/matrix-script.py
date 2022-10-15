# https://www.hackerrank.com/challenges/matrix-script/problem

import re

n, m = map(int, input().split())

b = "".join(["".join(i) for i in zip(*[input() for _ in range(n)])])

print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", b))
