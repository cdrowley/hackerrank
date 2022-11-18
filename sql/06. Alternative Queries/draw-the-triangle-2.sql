-- https://www.hackerrank.com/challenges/draw-the-triangle-2/
SELECT TOP 20 REPLICATE('* ', ROW_NUMBER() OVER(ORDER BY sys.all_objects.name)) AS display
FROM sys.all_objects
;
