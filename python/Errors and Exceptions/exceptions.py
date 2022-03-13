# https://www.hackerrank.com/challenges/exceptions/problem

tries = range(int(input()))

for _ in tries:
    try:
        a, b = map(int, input().split())
        print(a // b)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)
