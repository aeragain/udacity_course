import fresh_tomatoes
import movie_data

# get movie instances and open page
movies = movie_data.get_movies()
fresh_tomatoes.open_movies_page(movies)
