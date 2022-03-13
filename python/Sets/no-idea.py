# https://www.hackerrank.com/challenges/no-idea/problem

_ = input()

int_list = lambda: map(int, input().split())
arr, good, bad = int_list(), set(int_list()), set(int_list())
print(sum((n in good) - (n in bad) for n in arr))
