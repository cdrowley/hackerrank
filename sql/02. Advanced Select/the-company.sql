-- https://www.hackerrank.com/challenges/the-company/
select c.company_code,
    c.founder,
    count(distinct lm.lead_manager_code),
    count(distinct sm.senior_manager_code),
    count(distinct m.manager_code),
    count(distinct e.employee_code)
from company c
    join lead_manager lm ON lm.company_code = c.company_code
    join senior_manager sm ON sm.lead_manager_code = lm.lead_manager_code
    join manager m ON m.senior_manager_code = sm.senior_manager_code
    join employee e ON e.manager_code = m.manager_code
group by c.company_code,
    founder
order by c.company_code;