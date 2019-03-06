-- list all genres taht are not associated with Dexter
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.id NOT IN (
	SELECT tv_genres.id
	FROM tv_genres LEFT JOIN (tv_show_genres CROSS JOIN tv_shows)
	ON (tv_shows.id = tv_show_genres.show_id 
		AND tv_show_genres.genre_id = tv_genres.id)
	WHERE title = "Dexter")
ORDER BY tv_genres.name ASC;
