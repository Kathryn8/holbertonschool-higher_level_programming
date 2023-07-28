-- Import the database dump from hbtn_0d_tvshows to your MySQL server
SELECT title, genre_id FROM tv_shows A INNER JOIN tv_show_genres B ON A.id = B.show_id ORDER BY title, genre_id;
