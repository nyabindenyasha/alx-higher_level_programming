-- inserts a new row in the table first_table 
-- database hbtn_0c_0
SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
