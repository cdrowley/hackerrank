-- https://www.hackerrank.com/challenges/weather-observation-station-14/
SELECT TOP 1 CAST(lat_n AS DECIMAL (10, 4)) AS lat_n
FROM
  station
WHERE
  lat_n < 137.2345
ORDER BY
  lat_n DESC
;
