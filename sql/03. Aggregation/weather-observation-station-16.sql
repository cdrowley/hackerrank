-- https://www.hackerrank.com/challenges/weather-observation-station-16/
select top 1 cast(lat_n as decimal(18, 4))
from station
where lat_n > 38.7780
order by lat_n;