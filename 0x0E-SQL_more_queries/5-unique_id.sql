-- Creates table y in dtb argv with unique id & def 1

CREATE TABLE IF NOT EXISTS unique_id (
 id INT DEFAULT 1 UNIQUE,
 name VARCHAR(256)
);
