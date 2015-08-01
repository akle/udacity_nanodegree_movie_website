import media
import fresh_tomatoes

#We create a couple of movies
toy_story = media.Movie("Toy Story", "Toys that behave like people",  "https://www.movieposter.com/posters/archive/main/98/MPW-49351", "www.youtube.com/watch?v=3jC6McxjCnE")

avatar = media.Movie("Avatar", "Blue people with guns.", "http://www.impawards.com/2009/posters/avatar_ver5.jpg", "https://www.youtube.com/watch?v=cX0R3mXaod8")

#Store the movies in an array.
movies = [toy_story, avatar]

#Pass the array to the page maker.
fresh_tomatoes.open_movies_page(movies)