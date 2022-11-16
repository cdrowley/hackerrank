-- https://www.hackerrank.com/challenges/full-score/
SELECT
    s.hacker_id
  , h.name
FROM
    submissions s
    INNER JOIN hackers h ON h.hacker_id = s.hacker_id
    INNER JOIN challenges c ON c.challenge_id = s.challenge_id
    INNER JOIN difficulty d ON d.difficulty_level = c.difficulty_level
    AND s.score = d.score
GROUP BY
    s.hacker_id
  , h.name
HAVING
    COUNT(DISTINCT s.challenge_id) > 1
ORDER BY
    COUNT(DISTINCT s.challenge_id) desc
  , s.hacker_id
  , h.name
;