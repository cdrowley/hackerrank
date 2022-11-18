-- https://www.hackerrank.com/challenges/weather-observation-station-5/
SELECT TOP 1
  city
  , LEN(city) AS shortest
FROM
  station
ORDER BY
  LEN(city)
  , city
;

SELECT TOP 1
  city
  , LEN(city) AS longest
FROM
  station
ORDER BY
  LEN(city) DESC
;
