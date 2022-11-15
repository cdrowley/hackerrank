-- https://www.hackerrank.com/challenges/weather-observation-station-20/
select distinct
    cast(
        round(
            percentile_disc(0.5) within group (
                order by
                    lat_n
            ) over ()
          , 4
        ) as decimal (16, 4)
    )
from
    station
;