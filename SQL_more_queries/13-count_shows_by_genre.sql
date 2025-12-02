-- List number of shows per genre
SELECT genre_id AS genre,
       COUNT(show_id) AS number_of_shows
FROM tv_show_genres
GROUP BY genre_id
ORDER BY number_of_shows DESC;
