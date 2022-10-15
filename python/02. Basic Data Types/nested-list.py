# https://www.hackerrank.com/challenges/nested-list/problem

n = int(input())
student_scores = [(input(), float(input())) for _ in range(n)]
second_lowest = sorted({ss[1] for ss in student_scores})[1]
second_lowest_scorers = [ss[0] for ss in student_scores if ss[1] == second_lowest]
second_lowest_scorers.sort()

for student in second_lowest_scorers:
    print(student)
