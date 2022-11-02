-- inserts a new row in the table first_table 
-- database hbtn_0c_0
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month>=7 AND month<=8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
