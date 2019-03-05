-- list all the records with the same score and the count.
SELECT score, COUNT(*) FROM second_table GROUP BY score DESC;
