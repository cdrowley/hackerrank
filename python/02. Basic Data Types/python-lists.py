# https://www.hackerrank.com/challenges/python-lists/problem

n = int(input())
arr = []

for _ in range(n):
    cmd = input().split()
    cmd_len = len(cmd)

    if "print" in cmd:
        print(arr)
        continue
    elif cmd_len == 1:
        cmd = f"arr.{cmd[0]}()"
    elif cmd_len == 2:
        cmd = f"arr.{cmd[0]}({cmd[1]})"
    else:
        cmd = f"arr.{cmd[0]}({cmd[1]}, {cmd[2]})"

    eval(cmd)
