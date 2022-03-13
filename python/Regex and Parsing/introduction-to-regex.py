# https://www.hackerrank.com/challenges/introduction-to-regex/problem

import re

pattern = "^[-+]?[\d]*\.[\d]+$"

for _ in range(int(input())):
    print(bool(re.match(pattern, input())))
