-- https://www.hackerrank.com/challenges/occupations/
select [Doctor],
    [Professor],
    [Singer],
    [Actor]
from (
        select row_number() over (
                partition by occupation
                order by name
            ) [RowNumber],
            *
        from occupations
    ) as tempTable pivot (
        max(name) FOR OCCUPATION in ([Doctor], [Professor], [Singer], [Actor])
    ) as pivotTable;