-- https://www.hackerrank.com/challenges/the-blunder/
select 1 + round(
        avg(salary) - avg(cast(replace(salary, "0", "") as integer)),
        0
    )
from employees;