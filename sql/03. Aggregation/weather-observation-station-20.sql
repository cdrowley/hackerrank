-- https://www.hackerrank.com/challenges/weather-observation-station-20/
SELECT DISTINCT CAST(ROUND(PERCENTILE_DISC(0.5) WITHIN GROUP (ORDER BY lat_n ASC) OVER (), 4) AS DECIMAL (16, 4)) AS median_lat
FROM station
;
