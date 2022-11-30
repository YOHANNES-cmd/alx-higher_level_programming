-- Lists all shows contained in the database hbtn_0d_tvshows without a
-- genre linked.
SELECT tv_genres.name AS name FROM tv_show_genres INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id WHERE tv_shows.title = 'Dexter' ORDER BY name;
