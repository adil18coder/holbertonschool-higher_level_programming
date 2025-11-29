-- List all records where name is not NULL, ordered by score descending
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
