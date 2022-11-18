-- https://www.hackerrank.com/challenges/weather-observation-station-19/
SELECT CAST(
    SQRT(
      SQUARE(ABS(MAX(lat_n)) - ABS(MIN(lat_n))) + (SQUARE(ABS(MAX(long_w)) - ABS(MIN(long_w))))
    ) AS DECIMAL (10, 4)
  ) AS distance
FROM
  station
;
