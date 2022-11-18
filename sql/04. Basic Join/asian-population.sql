-- https://www.hackerrank.com/challenges/asian-population/
SELECT SUM(c.population) AS population
FROM
  city c
INNER JOIN country co ON c.countrycode = co.code
WHERE
  co.continent = 'Asia'
;
