-- inserts a new row in the table first_table 
-- database hbtn_0c_0
SELECT score, COUNT(score) AS "number" FROM second_table GROUP BY score DESC;
