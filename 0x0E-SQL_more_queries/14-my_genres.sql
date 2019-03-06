-- list the genres for the tv show dexter
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN (tv_show_genres CROSS JOIN tv_shows)
ON (tv_genres.id = tv_show_genres.genre_id
AND tv_show_genres.show_id = tv_shows.id)
WHERE tv_shows.title = 'Dexter';
