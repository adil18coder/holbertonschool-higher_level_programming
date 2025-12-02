-- List all TV shows that belong to the Comedy genre
SELECT s.title
FROM tv_shows s
JOIN tv_show_genres tg ON s.id = tg.show_id
JOIN tv_genres g ON tg.genre_id = g.id
WHERE g.name = 'Comedy'
ORDER BY s.title ASC;
