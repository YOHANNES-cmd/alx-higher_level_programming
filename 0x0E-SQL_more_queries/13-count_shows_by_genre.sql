-- Lists all shows contained in the database hbtn_0d_tvshows without a
-- genre linked.
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows FROM tv_genres INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id GROUP BY tv_genres.id ORDER BY number_of_shows DESC;
