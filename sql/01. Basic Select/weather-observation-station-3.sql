-- https://www.hackerrank.com/challenges/weather-observation-station-3/
select city
from station
where lat_n > 0
    and long_w > 0
    and id % 2 = 0
group by city;