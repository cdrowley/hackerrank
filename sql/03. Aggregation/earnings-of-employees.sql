-- https://www.hackerrank.com/challenges/earnings-of-employees/
/*
 with cte(earnings, employee_cnt) as (
 select salary * months,
 count(name)
 from employee
 group by salary * months
 )
 select top(1) *
 from cte
 order by earnings desc;
 */
with workings as (
    select max(salary * months) over() top_salary,
        case
            when (salary * months) = max(salary * months) over() then 1
            else 0
        END earns_top_salary
    from employee
)
select max(top_salary),
    sum(earns_top_salary)
from workings;