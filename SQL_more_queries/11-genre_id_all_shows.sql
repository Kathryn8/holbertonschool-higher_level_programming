-- script that lists all shows contained in the database hbtn_0d_tvshows
SELECT title, genre_id FROM tv_shows A LEFT JOIN tv_show_genres B ON A.id = B.show_id ORDER BY title, genre_id;
