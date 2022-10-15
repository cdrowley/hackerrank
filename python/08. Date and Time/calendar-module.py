# https://www.hackerrank.com/challenges/calendar-module/problem

import calendar

# print(calendar.TextCalendar(firstweekday=6).formatyear(2015))

mm, dd, yyyy = map(int, input().split())
date = calendar.weekday(yyyy, mm, dd)
days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
print(days[date])
