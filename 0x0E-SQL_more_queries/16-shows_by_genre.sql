-- Lists all comedy shows in the database hbtn_0d_tvshows.
SELECT tv_shows.title AS title, tv_genres.name AS name FROM tv_show_genres INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id RIGHT OUTER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id ORDER BY title, name;
