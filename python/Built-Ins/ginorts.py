# https://www.hackerrank.com/challenges/ginorts/problem

s_input = input()

lowers = sorted([c for c in s_input if c.isalpha() and c.islower()])
uppers = sorted([c for c in s_input if c.isalpha() and c.isupper()])
odds = sorted([c for c in s_input if c.isdigit() and int(c) % 2 == 1])
evens = sorted([c for c in s_input if c.isdigit() and int(c) % 2 == 0])

print("".join(lowers + uppers + odds + evens))
