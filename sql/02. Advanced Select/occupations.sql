-- https://www.hackerrank.com/challenges/occupations/
WITH
enummerated AS (
  SELECT
    *
    , ROW_NUMBER() OVER (
      PARTITION BY
      occupation
      ORDER BY
        name
    ) AS rn
  FROM
    occupations
)

SELECT
  doctor
  , professor
  , singer
  , actor
FROM
  enummerated PIVOT (
  MAX(name) FOR occupation IN (doctor, professor, singer, actor)
) AS pivotted
;
