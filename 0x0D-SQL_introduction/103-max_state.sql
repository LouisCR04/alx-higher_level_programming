-- Displays max temp of each state ordered by state name
-- Ordered by State

SELECT state, MAX(value) AS Max_temp
 FROM temperatures
 GROUP by state
 ORDER BY state ASC;
