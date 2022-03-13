# https://www.hackerrank.com/challenges/symmetric-difference/problem

_ = input()
a = set(map(int, input().split()))

_ = input()
b = set(map(int, input().split()))

for i in sorted(a ^ b):
    print(i)
