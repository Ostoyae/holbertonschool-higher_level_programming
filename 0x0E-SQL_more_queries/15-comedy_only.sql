-- list all comedy shows
SELECT tv_shows.title
FROM tv_show_genres INNER JOIN (tv_shows CROSS JOIN tv_genres)
ON (tv_shows.id = tv_show_genres.show_id 
	AND tv_show_genres.genre_id = tv_genres.id)
WHERE tv_genres.name = "Comedy"
ORDER BY tv_shows.title ASC;
