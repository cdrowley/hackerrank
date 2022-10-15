# https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re

N = int(input())
PATTERN = r"^(7|8|9)\d{9}$"

for _ in range(N):
    UI = input()
    matchObj = re.search(PATTERN, UI)
    print("YES" if matchObj else "NO")
