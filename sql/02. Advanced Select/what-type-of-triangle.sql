-- https://www.hackerrank.com/challenges/what-type-of-triangle/
SELECT CASE
    WHEN (
      a + b <= c
      OR a + c <= b
      OR b + c <= a
    ) THEN 'Not A Triangle'
    WHEN (
      a = b
      AND b = c
    ) THEN 'equilateral'
    WHEN (
      a = b
      OR b = c
      OR a = c
    ) THEN 'isosceles'
    ELSE 'scalene'
  END AS triangle_type
FROM
  triangles
;
