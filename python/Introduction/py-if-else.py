# https://www.hackerrank.com/challenges/py-if-else/problem

n = int(input().strip())

print("Weird" if n % 2 == 1 or n in range(6, 21, 2) else "Not Weird")
