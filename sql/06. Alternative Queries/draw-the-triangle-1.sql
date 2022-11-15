-- https://www.hackerrank.com/challenges/draw-the-triangle-1/
DECLARE @i INT = 20;
WHILE @i > 0 BEGIN print replicate('* ', @i)
SET @i = @i -1;
END;