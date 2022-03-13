# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

_ = int(input())

shoe_sizes = Counter(map(int, input().split()))
customers = int(input())

revenue = 0
for _ in range(customers):
    size, price = map(int, input().split())
    if size in shoe_sizes.keys():
        if shoe_sizes[size] > 0:
            revenue += price
            shoe_sizes[size] -= 1
print(revenue)
