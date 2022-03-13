# https://www.hackerrank.com/challenges/find-angle/problem

from math import degrees, atan

ab, bc = [float(input()) for _ in range(2)]
deg = "\xb0"

print(f"{int(round(degrees(atan(ab/bc)), 0))}{deg}")
