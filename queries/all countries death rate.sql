-- COUNTRY AND DEAT RATE
SELECT [Country/Region],
       -- CALCULATE DEAT RATE
       CAST(SUM(Deaths) AS FLOAT) / NULLIF(SUM(Confirmed),0) AS death_rate
FROM covid
-- GROUP
GROUP BY [Country/Region]
-- SORT
ORDER BY death_rate DESC;

