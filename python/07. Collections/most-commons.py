# https://www.hackerrank.com/challenges/most-commons/problem

from collections import Counter

[print(*i) for i in sorted(Counter(input()).items(), key=lambda x: (-x[1], x[0]))[:3]]
