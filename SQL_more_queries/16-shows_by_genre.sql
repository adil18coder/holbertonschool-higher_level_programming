-- List all TV shows along with their genres (NULL if no genre)
SELECT s.title, g.name
FROM tv_shows s
LEFT JOIN tv_show_genres tg ON s.id = tg.show_id
LEFT JOIN tv_genres g ON tg.genre_id = g.id
ORDER BY s.title ASC, g.name ASC;

