# https://www.hackerrank.com/challenges/iterables-and-iterators/problem

from itertools import combinations

_ = int(input())

letters = input().split()
length = int(input())

outcomes = list(combinations(letters, length))
desired_outcomes = [o for o in outcomes if "a" in o]
print(round(len(desired_outcomes) / len(outcomes), 3))
