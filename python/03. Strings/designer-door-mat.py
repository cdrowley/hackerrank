# https://www.hackerrank.com/challenges/designer-door-mat/problem

height, width = map(int, input().split())


top = [(i * ".|.").center(width, "-") for i in range(1, height, 2)]
mid = "WELCOME".center(width, "-")
bot = [(i * ".|.").center(width, "-") for i in range(height - 2, -1, -2)]
print("\n".join(top), mid, "\n".join(bot), sep="\n")
