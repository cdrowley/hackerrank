-- https://www.hackerrank.com/challenges/weather-observation-station-17/
select cast(long_w as decimal(10, 4))
from station
where id in (
        select top 1 id
        from station
        where lat_n > 38.7780
        order by lat_n asc
    );