# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

_ = int(input())
s = set(map(int, input().split()))

commands = [input().split() for _ in range(int(input()))]
commands = [
    "s.{}({})".format(i[0], i[1]) if len(i) > 1 else "s.{}()".format(i[0])
    for i in commands
]

for c in commands:
    eval(c)

print(sum(s))
