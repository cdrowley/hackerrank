-- https://www.hackerrank.com/challenges/contest-leaderboard/
WITH
  max_challenge_scores AS (
    SELECT
      hacker_id
    , challenge_id
    , MAX(score) AS max_score
    FROM
      submissions
    GROUP BY
      hacker_id
    , challenge_id
  )
SELECT
  h.hacker_id
, h.name
, SUM(max_score) AS total_score
FROM
  hackers h
  INNER JOIN max_challenge_scores ms ON h.hacker_id = ms.hacker_id
GROUP BY
  h.hacker_id
, h.name
HAVING
  SUM(ms.max_score) > 0
ORDER BY
  SUM(ms.max_score) DESC
, h.hacker_id
;