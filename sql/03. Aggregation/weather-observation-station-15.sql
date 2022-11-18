-- https://www.hackerrank.com/challenges/weather-observation-station-15/
SELECT CAST(MAX(long_w) AS DECIMAL (18, 4)) AS long_w
FROM
  station
WHERE
  lat_n = (
    SELECT MAX(lat_n) AS lat_n
    FROM
      station
    WHERE
      lat_n < 137.2345
  )
;
