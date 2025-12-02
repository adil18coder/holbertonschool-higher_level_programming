-- List all genres of the show Dexter
SELECT g.name
FROM tv_genres g
JOIN tv_show_genres tg ON g.id = tg.genre_id
JOIN tv_shows s ON tg.show_id = s.id
WHERE s.title = "Dexter"
ORDER BY g.name ASC;

