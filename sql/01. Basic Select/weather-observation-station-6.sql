-- https://www.hackerrank.com/challenges/weather-observation-station-6/
SELECT
  city
FROM
  station
WHERE
  city LIKE 'a%'
  OR city LIKE 'e%'
  OR city LIKE 'i%'
  OR city LIKE 'o%'
  OR city LIKE 'u%'
GROUP BY
  city
;