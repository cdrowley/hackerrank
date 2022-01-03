# https://www.hackerrank.com/challenges/between-two-sets/problem

# O(n log(n)) solution.
# 1. find the LCM of all the integers of array A.
# 2. find the GCD of all the integers of array B.
# 3. Count the number of multiples of LCM that evenly divides the GCD.


from functools import reduce


def gcd(x: int, y: int) -> int:
    while y:
        x, y = y, x % y
    return x


def lcm(x: int, y: int) -> int:
    return (x * y) // gcd(x, y)


_ = input()
a = [int(i) for i in input().strip().split()]
b = [int(i) for i in input().strip().split()]

lcm_of_a = reduce(lcm, a)
gcd_of_b = reduce(gcd, b)

intersection = [m for m in range(lcm_of_a, gcd_of_b + 1, lcm_of_a) if gcd_of_b % m == 0]
print(len((intersection)))
