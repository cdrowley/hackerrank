-- https://www.hackerrank.com/challenges/weather-observation-station-14/
select top 1 cast(lat_n as decimal(10, 4))
from station
where lat_n < 137.2345
order by lat_n desc;