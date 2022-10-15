# https://www.hackerrank.com/challenges/python-loops/problem

n = [i**2 for i in range(int(input())) if i >= 0]
for i in n:
    print(i)
