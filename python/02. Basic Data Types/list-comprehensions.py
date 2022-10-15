# https://www.hackerrank.com/challenges/list-comprehensions/problem

x, y, z, n = (int(input()) for _ in range(4))

print(
    [
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if sum([i, j, k]) != n
    ]
)

# results = []
# for i in range(x + 1):
#     for j in range(y + 1):
#         for k in range(z + 1):
#             if sum([i, j, k]) == 2:
#                 continue
#             results.append([i, j, k])
