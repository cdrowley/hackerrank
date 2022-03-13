# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

_ = input()
print(sorted(set(map(int, input().split())))[-2])
