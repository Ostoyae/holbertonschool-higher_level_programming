-- list all comedy shows
SELECT tv_shows.title, tv_genres.name
FROM tv_shows LEFT JOIN (tv_show_genres CROSS JOIN tv_genres)
ON (tv_shows.id = tv_show_genres.show_id 
	AND tv_show_genres.genre_id = tv_genres.id)
ORDER BY tv_shows.title ASC;
