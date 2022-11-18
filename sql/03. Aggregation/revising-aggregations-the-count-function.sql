-- https://www.hackerrank.com/challenges/revising-aggregations-the-count-function/
SELECT COUNT(*) AS large_cities_cnt
FROM
  city
WHERE
  population > 100000
;
