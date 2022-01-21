--In 6.sql, write a SQL query to determine the average rating of all movies released in 2012.
--Your query should output a table with a single column and a single row (not including the header) containing the average rating.
SELECT AVG(rating)
FROM ratings
INNER JOIN rating ON movies.id = ratings.movie_id
WHERE movie_id = (SELECT id FROM movies WHERE year = 2012);

JOIN stars ON people.id = stars.person_id
   ...> JOIN shows ON stars.show_id = shows.id
   ...> WHERE name = "Steve Carell";