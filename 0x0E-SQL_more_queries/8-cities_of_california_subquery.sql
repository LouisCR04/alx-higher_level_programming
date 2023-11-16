-- Lists all cities of California that can be found in the dtb argv

SELECT id, name
 FROM cities
 WHERE state_id = (
  SELECT id
   FROM states
   WHERE name = 'California'
  );
