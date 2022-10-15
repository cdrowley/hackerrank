# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem


def fibonacci(n):
    output = [0, 1]
    for i in range(2, n):
        output.append(output[i - 2] + output[i - 1])
    return output[0:n]


cube = lambda x: x**3
