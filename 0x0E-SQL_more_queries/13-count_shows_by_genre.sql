-- list all show in hbtn_0d_tvshows
SELECT tv_genres.name AS genre,
COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_show_genres INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY name
ORDER BY COUNT(tv_show_genres.genre_id) DESC;
