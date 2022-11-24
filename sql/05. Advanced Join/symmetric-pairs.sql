-- https://www.hackerrank.com/challenges/symmetric-pairs
SELECT
  a.x
  , a.y
FROM functions a
INNER JOIN functions b
  ON a.x = b.y
    AND a.y = b.x
GROUP BY a.x, a.y
HAVING COUNT(a.x) > 1 OR a.x < a.y
ORDER BY a.x
;
