# https://www.hackerrank.com/challenges/python-mod-divmod/problem

ans = divmod(*[int(input()) for _ in range(2)])
print(ans[0], ans[1], ans, sep="\n")
