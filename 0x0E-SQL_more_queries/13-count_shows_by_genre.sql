-- lists all privileges of the MySQL users user_0d_1 and user_0d_2
-- SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
-- LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title, tv_show_genres.genre_id;
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id GROUP BY tv_show_genres.genre_id ORDER BY number_of_shows DESC;
