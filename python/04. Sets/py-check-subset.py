# https://www.hackerrank.com/challenges/py-check-subset/problem

N = int(input())

for _ in range(N):
    input()
    A = set(input().split())
    input()
    B = set(input().split())
    print(A.issubset(B))
