-- https://www.hackerrank.com/challenges/the-pads/
WITH
  cte AS (
    SELECT
      occupation
    , COUNT(LEFT (occupation, 1)) AS letter
    FROM
      occupations
    GROUP BY
      occupation
  )
SELECT
  CONCAT (name, "(", LEFT (occupation, 1), ")")
FROM
  occupations
UNION
SELECT
  CONCAT (
    "There are a total of "
  , letter
  , " "
  , LOWER(occupation)
  , "s."
  )
FROM
  cte
;