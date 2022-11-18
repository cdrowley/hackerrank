-- https://www.hackerrank.com/challenges/weather-observation-station-3/
SELECT city
FROM
  station
WHERE
  lat_n > 0
  AND long_w > 0
  AND id % 2 = 0
GROUP BY
  city
;
