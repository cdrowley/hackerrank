-- https://www.hackerrank.com/challenges/weather-observation-station-8/
SELECT DISTINCT city
FROM
  station
WHERE
  LEFT(city, 1) IN ('a', 'e', 'i', 'o', 'u')
  AND RIGHT(city, 1) IN ('a', 'e', 'i', 'o', 'u')
;
