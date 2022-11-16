-- https://www.hackerrank.com/challenges/asian-population/
SELECT
    SUM(city.population)
FROM
    city
    JOIN country ON CITY.countrycode = country.code
WHERE
    country.continent = 'Asia'
;