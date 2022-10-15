-- https://www.hackerrank.com/challenges/weather-observation-station-18/
select cast(
        (
            abs(max(lat_n) - min(lat_n)) + abs(max(long_w) - min(long_w))
        ) as numeric(18, 4)
    )
from station;