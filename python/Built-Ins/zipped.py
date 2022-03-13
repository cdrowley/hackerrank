# https://www.hackerrank.com/challenges/zipped/problem

N, X = map(int, input().split())

grades = [list(map(float, input().split())) for _ in range(X)]

for i in zip(*grades):
    print(sum(i) / len(i))
