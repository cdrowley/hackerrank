-- https://www.hackerrank.com/challenges/interviews
WITH views
AS (
  SELECT
    c.contest_id
    , SUM(vs.total_views) AS total_views
    , SUM(vs.total_unique_views) AS total_unique_views
  FROM contests c
  INNER JOIN colleges co ON c.contest_id = co.contest_id
  INNER JOIN challenges ch ON ch.college_id = co.college_id
  INNER JOIN view_stats vs ON vs.challenge_id = ch.challenge_id
  GROUP BY c.contest_id
)

, submissions
AS (
  SELECT
    a.contest_id
    , SUM(ss.total_submissions) AS total_submissions
    , SUM(ss.total_accepted_submissions) AS total_accepted_submissions
  FROM contests a
  INNER JOIN colleges b ON a.contest_id = b.contest_id
  INNER JOIN challenges ch ON ch.college_id = b.college_id
  INNER JOIN submission_stats ss ON ss.challenge_id = ch.challenge_id
  GROUP BY a.contest_id
)

SELECT
  c.contest_id
  , c.hacker_id
  , c.name
  , s.total_submissions
  , s.total_accepted_submissions
  , v.total_views
  , v.total_unique_views
FROM contests c
INNER JOIN views v ON c.contest_id = v.contest_id
INNER JOIN submissions s ON c.contest_id = s.contest_id
WHERE s.total_submissions > 0
  OR s.total_accepted_submissions > 0
  OR v.total_views > 0
  OR v.total_unique_views > 0
;
