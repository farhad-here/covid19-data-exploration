-- ACTIVE RECOVERED
SELECT [Country/Region],
SUM(Active) active_cases,
SUM(Recovered) recovered
FROM covid
GROUP BY [Country/Region]
ORDER BY active_cases DESC;