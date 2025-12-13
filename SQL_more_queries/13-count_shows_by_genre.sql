-- Holberton: TV shows janr və say hesablaması
SELECT g.name AS genre, COUNT(sg.show_id) AS number_of_shows
FROM tv_genres g
JOIN tv_show_genres sg ON g.id = sg.genre_id
GROUP BY g.id
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
