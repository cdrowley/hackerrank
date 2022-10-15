-- https://www.hackerrank.com/challenges/more-than-75-marks/
select distinct city
from station
where left(city, 1) not in ('a', 'e', 'i', 'o', 'u')
    and right(city, 1) not in ('a', 'e', 'i', 'o', 'u')