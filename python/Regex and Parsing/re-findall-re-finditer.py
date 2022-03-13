# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem

import re

# CONS = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'
# VOWS = 'AEIOUaeiou'
PATTERN = "(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])[AEIOUaeiou]{2,}(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])"

S = input()
M = re.findall(PATTERN, S)

if M:
    for i in M:
        print(i)
else:
    print("-1")
