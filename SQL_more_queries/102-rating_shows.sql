-- script that lists all shows from hbtn_0d_tvshows_rate by their rating
SELECT title, SUM(rate) AS rating
FROM tv_show_ratings a
INNER JOIN tv_shows b
      ON a.show_id = b.id
GROUP BY show_id
ORDER BY rating DESC;
