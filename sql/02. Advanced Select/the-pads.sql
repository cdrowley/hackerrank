-- https://www.hackerrank.com/challenges/the-pads/
WITH
count_occupations AS (
  SELECT
    occupation
    , COUNT(LEFT(occupation, 1)) AS letter
  FROM
    occupations
  GROUP BY
    occupation
)

SELECT CONCAT(name, '(', LEFT(occupation, 1), ')') AS name
FROM
  occupations
UNION
SELECT CONCAT(
    'There are a total of '
    , letter
    , ' '
    , LOWER(occupation)
    , 's.'
  ) AS total
FROM
  count_occupations
;
