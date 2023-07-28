-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT name
FROM tv_genres a
INNER JOIN tv_show_genres b
      ON a.id = b.genre_id
INNER JOIN tv_shows c
      ON b.show_id = c.id
WHERE title = 'Dexter'
ORDER BY name;
