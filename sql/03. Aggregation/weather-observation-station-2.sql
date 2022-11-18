-- https://www.hackerrank.com/challenges/weather-observation-station-2/
SELECT
  ROUND(CAST(SUM(lat_n) AS DECIMAL (16, 2)), 2) AS lat_n
  , ROUND(CAST(SUM(long_w) AS DECIMAL (16, 2)), 2) AS long_w
FROM
  station
;
