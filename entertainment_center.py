import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "http://ia.media-imdb.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#def__init__(self) and the self is Toy Story
#print(toy_story.storyline)
#toy_story.show_trailer()

avatar = media.Movie("Avatar", "\nA Marine on an Alien Planet",
                     "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

batman_dark_knight_rises = media.Movie("Batman: The Dark Knight Rises", "\nRise of the Ra'as Al Gul's Daughter and Fall of the Gotham",
                                       "http://ia.media-imdb.com/images/M/MV5BMTk4ODQzNDY3Ml5BMl5BanBnXkFtZTcwODA0NTM4Nw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                                       "https://www.youtube.com/watch?v=GokKUqLcvD8")

ratatouille = media.Movie("Ratatouille", "\nA rat is a chef in Paris",
                          "http://ia.media-imdb.com/images/M/MV5BMTMzODU0NTkxMF5BMl5BanBnXkFtZTcwMjQ4MzMzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

hunger_games = media.Movie("Hunger Games", "\nA really real reality show",
                           "http://ia.media-imdb.com/images/M/MV5BMjA4NDg3NzYxMF5BMl5BanBnXkFtZTcwNTgyNzkyNw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")



movies = (toy_story, avatar, batman_dark_knight_rises, ratatouille, hunger_games)
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
