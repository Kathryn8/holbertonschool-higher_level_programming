-- script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT s.title
FROM tv_shows s
LEFT JOIN
     (SELECT a.title
     FROM tv_shows a
     INNER JOIN tv_show_genres b
     	   ON a.id = b.show_id
     INNER JOIN tv_genres c
     	   ON b.genre_id = c.id
     WHERE c.name = 'Comedy') c
     ON s.title = c.title
WHERE c.title IS NULL
ORDER BY title;
