-- https://www.hackerrank.com/challenges/weather-observation-station-13/
SELECT
  CAST(SUM(lat_n) AS DECIMAL(10, 4))
FROM
  station
WHERE
  lat_n BETWEEN 38.7880 AND 137.2345
;