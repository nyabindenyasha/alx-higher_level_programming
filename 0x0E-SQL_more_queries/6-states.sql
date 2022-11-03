-- lists all privileges of the MySQL users user_0d_1 and user_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT UNIQUE AUTO_INCREMENT, name VARCHAR(256), PRIMARY KEY (id));
