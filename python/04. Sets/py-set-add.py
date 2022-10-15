# https://www.hackerrank.com/challenges/py-set-add/problem


unique_countries = set()
for _ in range(int(input())):
    unique_countries.add(input())

print(len(unique_countries))
