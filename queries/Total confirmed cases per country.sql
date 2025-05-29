-- country and number of confirmed covid per country
SELECT [Country/Region],SUM(Confirmed) AS total_confirmed
FROM covid
-- Group country
GROUP BY [Country/Region]
-- sort
ORDER BY total_confirmed DESC;