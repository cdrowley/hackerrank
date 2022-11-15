-- https://www.hackerrank.com/challenges/binary-search-tree-1/
SELECT
  N
, CASE
    WHEN P IS NULL THEN "Root"
    WHEN n IN (
      SELECT
        p
      FROM
        bst
    ) THEN "Inner"
    ELSE "Leaf"
  END
FROM
  bst
ORDER BY
  n
;