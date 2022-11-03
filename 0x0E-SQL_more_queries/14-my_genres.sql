-- lists all privileges of the MySQL users user_0d_1 and user_0d_2
-- SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
-- LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title, tv_show_genres.genre_id;
SELECT tv_genres.name FROM tv_show_genres
INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id 
WHERE tv_shows.title = "Dexter" ORDER BY tv_genres.name;
