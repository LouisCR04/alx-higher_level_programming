-- Lists all records of table x of dtb argv
-- Doesn't list a row without a name value

SELECT score, name
 FROM second_table
 WHERE `name` IS NOT NULL
 ORDER BY score DESC;
