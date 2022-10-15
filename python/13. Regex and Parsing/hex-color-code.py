# https://www.hackerrank.com/challenges/hex-color-code/problem

import re

for _ in range(int(input())):
    hexes = re.findall("[\s:](#[A-Fa-f0-9]{6}|#[A-Fa-f0-9]{3})", input())
    if hexes:
        print(*hexes, sep="\n")
