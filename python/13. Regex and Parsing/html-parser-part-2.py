# https://www.hackerrank.com/challenges/html-parser-part-2/problem


import re, sys

PATTERN = r"<!--((?:.+\n)+?.*)-->|<!--(.+)-->|<\w+[^>]*>([^<]+)<"

for m in re.finditer(PATTERN, sys.stdin.read()):
    titles = ["Multi-line Comment", "Single-line Comment", "Data"]
    print(f">>> {titles[m.lastindex - 1]}")
    for data in m.group(m.lastindex).split("\n"):
        print(data)
