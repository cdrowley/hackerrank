# https://www.hackerrank.com/challenges/word-order/problem

unique_words = {}
for _ in range(int(input())):
    UI = input()
    unique_words.setdefault(UI, 0)
    unique_words[UI] += 1

print(len(unique_words))
print(*unique_words.values())
