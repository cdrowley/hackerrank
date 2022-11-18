-- https://www.hackerrank.com/challenges/the-company/
SELECT
  c.company_code
  , c.founder
  , COUNT(DISTINCT lm.lead_manager_code) AS lead_managers
  , COUNT(DISTINCT sm.senior_manager_code) AS senior_managers
  , COUNT(DISTINCT m.manager_code) AS managers
  , COUNT(DISTINCT e.employee_code) AS employees
FROM
  company c
INNER JOIN lead_manager lm ON lm.company_code = c.company_code
INNER JOIN senior_manager sm ON sm.lead_manager_code = lm.lead_manager_code
INNER JOIN manager m ON m.senior_manager_code = sm.senior_manager_code
INNER JOIN employee e ON e.manager_code = m.manager_code
GROUP BY
  c.company_code
  , c.founder
ORDER BY
  c.company_code
;
