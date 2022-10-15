-- https://www.hackerrank.com/challenges/the-pads/
with cte as (
    select occupation,
        count(left(occupation, 1)) as letter
    from occupations
    group by occupation
)
select concat(name, "(", left(occupation, 1), ")")
from occupations
union
select concat(
        "There are a total of ",
        letter,
        " ",
        lower(occupation),
        "s."
    )
from cte;