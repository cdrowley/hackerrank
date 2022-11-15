-- https://www.hackerrank.com/challenges/occupations/
SELECT
  [Doctor]
, [Professor]
, [Singer]
, [Actor]
FROM
  (
    SELECT
      ROW_NUMBER() OVER (
        PARTITION BY
          occupation
        ORDER BY
          name
      ) [RowNumber]
    , *
    FROM
      occupations
  ) AS tempTable PIVOT (
    MAX(name) FOR OCCUPATION IN ([Doctor], [Professor], [Singer], [Actor])
  ) AS pivotTable
;