-- https://www.hackerrank.com/challenges/population-density-difference/
SELECT MAX(population) - MIN(population) AS population_difference
FROM
  city
;
