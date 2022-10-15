# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem

import re

n = int(input())

info = [input().split() for _ in range(n)]
valid_email = r"<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>"

for i in info:
    if re.match(valid_email, i[1]):
        print(" ".join(i))
