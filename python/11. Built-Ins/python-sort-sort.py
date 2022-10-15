# https://www.hackerrank.com/challenges/python-sort-sort/problem

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
arr.sort(key=lambda x: x[K])

[print(*el) for el in arr]
