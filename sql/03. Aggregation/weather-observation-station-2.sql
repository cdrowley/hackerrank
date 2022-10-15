-- https://www.hackerrank.com/challenges/weather-observation-station-2/
select round(cast(sum(lat_n) as decimal(16, 2)), 2),
    round(cast(sum(long_w) as decimal(16, 2)), 2)
from station;