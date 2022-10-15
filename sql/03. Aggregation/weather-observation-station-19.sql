-- https://www.hackerrank.com/challenges/weather-observation-station-19/
select cast(
        sqrt(
            square(abs(max(lat_n)) - abs(min(lat_n))) + (square(abs(max(long_w)) - abs(min(long_w))))
        ) as decimal(10, 4)
    )
from station