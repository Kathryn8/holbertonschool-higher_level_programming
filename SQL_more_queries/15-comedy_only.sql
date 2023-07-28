-- script that lists all Comedy shows in the database hbtn_0d_tvshows
SELECT title
FROM tv_shows a
INNER JOIN tv_show_genres b
      ON a.id = b.show_id
INNER JOIN tv_genres c
      ON b.genre_id = c.id
WHERE name = 'Comedy'
ORDER BY title;
