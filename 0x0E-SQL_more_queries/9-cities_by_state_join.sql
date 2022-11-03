-- lists all privileges of the MySQL users user_0d_1 and user_0d_2
SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id;
