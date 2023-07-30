--  script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT g.name
FROM tv_genres g
LEFT JOIN
     (SELECT a.name
     FROM tv_genres a
     INNER JOIN tv_show_genres b
           ON a.id = b.genre_id
     INNER JOIN tv_shows c
           ON b.show_id = c.id
     WHERE title = 'Dexter') d
     ON g.name = d.name
WHERE d.name IS NULL;
