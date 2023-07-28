--  script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT
	name AS genre,
	COUNT(genre_id) AS number_of_shows
FROM tv_show_genres a
INNER JOIN tv_genres b
      ON a.genre_id = b.id
GROUP BY genre_id
ORDER BY number_of_shows DESC;
