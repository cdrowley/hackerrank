-- https://www.hackerrank.com/challenges/weather-observation-station-1/
select city,
    state
from station
where lat_n > 0
    and long_w > 0;