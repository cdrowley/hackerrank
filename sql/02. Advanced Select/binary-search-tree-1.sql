-- https://www.hackerrank.com/challenges/binary-search-tree-1/
SELECT
  n
  , CASE
    WHEN p IS NULL THEN 'root'
    WHEN n IN (
      SELECT p
      FROM
        bst
    ) THEN 'Inner'
    ELSE 'leaf'
  END AS node_type
FROM
  bst
ORDER BY
  n
;
