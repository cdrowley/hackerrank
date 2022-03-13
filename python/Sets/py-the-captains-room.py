# https://www.hackerrank.com/challenges/py-the-captains-room/problem

from collections import Counter

_ = input()
rooms = Counter(input().split())
print(rooms.most_common()[-1][0])
