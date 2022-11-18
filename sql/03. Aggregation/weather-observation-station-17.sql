-- https://www.hackerrank.com/challenges/weather-observation-station-17/
SELECT TOP 1 CAST(long_w AS DECIMAL (10, 4)) AS long_w
FROM
  station
WHERE
  lat_n > 38.7780
ORDER BY
  lat_n ASC

;
