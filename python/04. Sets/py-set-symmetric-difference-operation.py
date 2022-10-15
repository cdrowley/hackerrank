# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

_, english_subs = input(), set(input().split())
_, french_subs = input(), set(input().split())

print(len(english_subs ^ french_subs))
