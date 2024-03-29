-- https://www.hackerrank.com/challenges/harry-potter-and-wands/
WITH
wands_filtered_and_ranked AS (
  SELECT
    w.id
    , wp.age
    , w.coins_needed
    , w.power
    , ROW_NUMBER() OVER (
      PARTITION BY
      wp.age
      , w.power
      ORDER BY
        w.coins_needed
    ) AS rn
  FROM
    wands w
  INNER JOIN wands_property wp ON w.code = wp.code
    AND wp.is_evil = 0
)

SELECT
  id
  , age
  , coins_needed
  , power
FROM
  wands_filtered_and_ranked
WHERE
  rn = 1
;
