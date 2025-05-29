SELECT [Country/Region],SUM(Confirmed) AS total_confirmed_iran_egypt
FROM covid
GROUP BY [Country/Region]
HAVING (SUM(Confirmed) IS NOT NULL) AND ([Country/Region] IN ('Iran','Egypt'))
ORDER BY total_confirmed_iran_egypt DESC;