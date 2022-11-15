-- https://www.hackerrank.com/challenges/the-blunder/
SELECT
  1 + ROUND(
    AVG(salary) - AVG(CAST(REPLACE(salary, "0", "") AS INTEGER))
  , 0
  )
FROM
  employees
;