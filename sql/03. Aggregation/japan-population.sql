-- https://www.hackerrank.com/challenges/japan-population/
SELECT SUM(population) AS population
FROM
  city
WHERE
  countrycode = 'JPN'
;
