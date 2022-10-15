# https://www.hackerrank.com/challenges/incorrect-regex/problem

import re


def isvalidregex(regex):
    try:
        re.compile(regex)
        return True
    except re.error:
        return False


test = [isvalidregex(input()) for _ in range(int(input()))]
for t in test:
    print(t)
