# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple

N, columns = int(input()), input().split()
Student = namedtuple("Student", ",".join(columns))
students = [Student(*(input().split())) for _ in range(N)]

print(f"{sum([int(s.MARKS) for s in students])/N:.2f}")
