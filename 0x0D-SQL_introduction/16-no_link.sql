-- List all records of table `second_table` with score and name in Desc order
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
