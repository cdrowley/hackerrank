-- https://www.hackerrank.com/challenges/weather-observation-station-15/
SELECT
  CAST(MAX(long_w) AS DECIMAL(18, 4))
FROM
  station
WHERE
  lat_n = (
    SELECT
      MAX(lat_n)
    FROM
      station
    WHERE
      lat_n < 137.2345
  )
;