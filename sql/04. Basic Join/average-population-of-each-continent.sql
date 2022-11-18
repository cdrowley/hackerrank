-- https://www.hackerrank.com/challenges/average-population-of-each-continent/
SELECT
  co.continent
  , FLOOR(AVG(c.population)) AS average_population
FROM
  city c
INNER JOIN country co ON c.countrycode = co.code
GROUP BY
  co.continent
;
