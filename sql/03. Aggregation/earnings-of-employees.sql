-- https://www.hackerrank.com/challenges/earnings-of-employees/
/*
with cte(earnings, employee_cnt) as (
select salary * months
, count(name)
from employee
group by salary * months
)
select top(1) *
from cte
order by earnings desc;
 */
WITH
workings AS (
  SELECT
    MAX(salary * months) OVER () AS top_salary
    , CASE
      WHEN (salary * months) = MAX(salary * months) OVER () THEN 1
      ELSE 0
    END AS earns_top_salary
  FROM
    employee
)

SELECT
  MAX(top_salary) AS top_salary
  , SUM(earns_top_salary) AS top_salary_cost
FROM
  workings
;
