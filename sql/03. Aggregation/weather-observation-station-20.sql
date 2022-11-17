-- https://www.hackerrank.com/challenges/weather-observation-station-20/
SELECT DISTINCT
    CAST(
        ROUND(
            PERCENTILE_DISC(0.5) within GROUP (
                ORDER BY
                    lat_n
            ) over ()
          , 4
        ) AS decimal (16, 4)
    )
FROM
    station
;