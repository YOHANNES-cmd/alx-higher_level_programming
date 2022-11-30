-- List all genres of the database hbtn_0d_tvshows
-- Not linkid to the show dexter.
-- Records are sorted by ascending genre name.
SELECT DISTINCT 'name' FROM 'tv_genres' AS g INNER JOIN 'tv_show_genre' AS s ON g.'id' = s.'genr_id' INNER JOIN 'tv_shows' AS t ON s.'show_id' = t.'id' WHERE g.'name' NOT IN (SELECT 'name' FROM 'tv_genres' AS g INNER JOIN 'tv_show_genres' AS s ON g.'id' = s.'genre_id' INNER JOIN 'tv_shows' AS t ON s.'show_id' = t.'id' WHERE t.'title' = "Dexter") ORDER BY g.'name';
