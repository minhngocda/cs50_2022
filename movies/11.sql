--In 11.sql, write a SQL query to list the titles of the five highest rated movies (in order) that Chadwick Boseman starred in, starting with the highest rated.
--Your query should output a table with a single column for the title of each movie.
--You may assume that there is only one person in the database with the name Chadwick Boseman.

--SELECT title FROM movies
--JOIN stars ON stars.movie_id = movies.id
--JOIN people ON people.id = stars.person_id WHERE name = "Chadwick Boseman"
--JOIN ratings ON ratings.movie_id = movies.id ORDER BY ratings.rating DESC LIMIT 5;
select movies.title from movies
join stars on stars.movie_id=movies.id
join people on stars.person_id=people.id
join ratings on ratings.movie_id=movies.id
where people.name="Chadwick Boseman"
order by ratings.rating desc
limit 5;