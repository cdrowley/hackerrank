-- https://www.hackerrank.com/challenges/african-cities/
SELECT c.name
FROM
  city c
INNER JOIN country co ON c.countrycode = co.code
WHERE
  co.continent = 'Africa'
;
