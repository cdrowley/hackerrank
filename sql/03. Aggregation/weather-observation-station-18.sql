-- https://www.hackerrank.com/challenges/weather-observation-station-18/
SELECT
  CAST(
    (
      ABS(MAX(lat_n) - MIN(lat_n)) + ABS(MAX(long_w) - MIN(long_w))
    ) AS NUMERIC(18, 4)
  )
FROM
  station
;