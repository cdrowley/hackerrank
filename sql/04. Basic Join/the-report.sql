-- https://www.hackerrank.com/challenges/the-report/
SELECT
  g.grade
  , s.marks
  , CASE
    WHEN g.grade < 8 THEN NULL
    ELSE s.name
  END AS name
FROM
  students s
LEFT JOIN grades g ON s.marks BETWEEN g.min_mark AND g.max_mark
ORDER BY
  g.grade DESC
  , s.name ASC
  , s.marks ASC
;
