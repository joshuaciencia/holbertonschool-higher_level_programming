-- list all cities in california
SELECT id, name FROM cities WHERE
state_id = (
SELECT id FROM states WHERE id = 1
) ORDER BY cities.id ASC;
