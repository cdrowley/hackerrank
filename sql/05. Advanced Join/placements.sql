-- https://www.hackerrank.com/challenges/placements/
WITH denormalised_salaries
AS (SELECT
    f.id
    , p.salary
    , f.friend_id
    , fp.salary AS friend_salary
  FROM friends f
  INNER JOIN packages AS p
    ON p.id = f.id
  INNER JOIN packages AS fp
    ON fp.id = f.friend_id
  WHERE fp.salary > p.salary
)

SELECT s.name
FROM students s INNER JOIN
  denormalised_salaries ds
  ON ds.id = s.id
ORDER BY ds.friend_salary
;
