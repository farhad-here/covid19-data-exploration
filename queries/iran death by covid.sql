SELECT [Country/Region], SUM(Deaths) AS Iran_death_by_covid
FROM covid

-- GROUP
GROUP BY [Country/Region]

HAVING (SUM(Deaths) IS NOT NULL) AND ([Country/Region] = ('Iran'))

-- SORT
ORDER BY Iran_death_by_covid DESC;