# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

A = set(input().split())
print(all(A.issuperset(set(input().split())) for _ in range(int(input()))))
