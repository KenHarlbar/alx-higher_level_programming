-- lists all cities contained in the database hbtn_0d_usa

SELECT cities.id, cities.name FROM cities
FROM cities
JOIN ON cities.state_id = states.id;