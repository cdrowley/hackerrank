-- https://www.hackerrank.com/challenges/weather-observation-station-16/
SELECT
  TOP 1 CAST(lat_n AS DECIMAL(18, 4))
FROM
  station
WHERE
  lat_n > 38.7780
ORDER BY
  lat_n
;