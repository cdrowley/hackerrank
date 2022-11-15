-- https://www.hackerrank.com/challenges/print-prime-numbers/
DECLARE @OUTPUT VARCHAR(1000) = '2';
DECLARE @NUM INT = 3;
-- for num in range(start=3, stop=1000, step=2):
WHILE @NUM < 1000 BEGIN
DECLARE @I INT = 2;
DECLARE @IS_PRIME BIT = 1;
-- for _ in range(start=i*i, stop=num, step=1)
WHILE @I * @I <= @NUM BEGIN IF @NUM % @I = 0
SET @IS_PRIME = 0;
SET @I + = 1;
END IF @IS_PRIME = 1
SET @OUTPUT = CONCAT(@OUTPUT, '&', @NUM);
SET @NUM + = 2;
END
SELECT @OUTPUT;