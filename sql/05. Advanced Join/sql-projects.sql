WITH
    project_start_date_groups AS (
        SELECT
            start_date
          , end_date
            /* 
            - tasks completed on consecutive end_dates will have the same project start day
            - incrementing by -1 on each row (ordering by end_date) allows those with the same project start date to be grouped 
            - we can ignore that the project_start_date won't be correct as we only need the grouping
            - for the actual project start date take MIN(start_date) and group by project_start_date_group
            
            start_date  | end_date     | -row_number() | project_start_date_group | project_start_grouping
            2015-11-11  | 2015-11-12   | -22           | 2015-10-21               | group 1
            2015-11-12  | 2015-11-13   | -23           | 2015-10-21               | group 1
            2015-11-17  | 2015-11-18   | -24           | 2015-10-25               | group 2
             */

          , DATEADD(
                DAY
              , - ROW_NUMBER() over (
                    ORDER BY
                        end_date
                )
              , end_date
            ) AS project_start_date_group
        FROM
            projects
    )
SELECT
    MIN(start_date)
  , MAX(end_date)
FROM
    project_start_date_groups
GROUP BY
    project_start_date_group
ORDER BY
    COUNT(project_start_date_group)
  , MIN(start_date)
;