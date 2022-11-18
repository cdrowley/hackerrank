-- https://www.hackerrank.com/challenges/revising-aggregations-sum/
SELECT SUM(population) AS population
FROM
  city
WHERE
  district = 'California'
;
