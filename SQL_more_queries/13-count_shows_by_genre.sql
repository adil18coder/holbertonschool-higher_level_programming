-- List number of shows per genre
SELECT g.name AS genre, COUNT(s.id) AS number_of_shows
FROM genres g
JOIN shows s ON s.genre_id = g.id
GROUP BY g.id
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
