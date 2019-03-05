-- list all the records with the same score and the count.
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score DESC;
