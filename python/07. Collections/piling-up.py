# https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque

T = int(input())

for _ in range(T):
    __ = input()

    blocks = deque(map(int, input().split()))

    for b in reversed(sorted(blocks)):
        if blocks[-1] == b:
            blocks.pop()
        elif blocks[0] == b:
            blocks.popleft()
        else:
            print("No")
            break
    else:
        print("Yes")
