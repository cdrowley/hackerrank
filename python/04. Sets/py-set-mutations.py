# https://www.hackerrank.com/challenges/py-set-mutations/problem


def get_input():
    c = input().split()
    set_ = set(map(int, input().split()))

    if len(c) == 1:
        return c, set_
    else:
        command_ = f"A.{c[0]}({set_})"
        return command_, set_


_, A = get_input()
num_other_sets = int(input())

for _ in range(num_other_sets):
    c, s = get_input()
    eval(c)

print(sum(A))
