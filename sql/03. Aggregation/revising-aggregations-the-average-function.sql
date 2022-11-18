-- https://www.hackerrank.com/challenges/revising-aggregations-the-average-function/
SELECT AVG(population) AS avg_pop
FROM
  city
WHERE
  district = 'California'
;
