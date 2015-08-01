import webbrowser

class Movie():
    """
    Creates a Movie.
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title =  movie_title
        self.storyline =  movie_storyline
        self.trailer_youtube_url = trailer_youtube
        self.poster_image_url = poster_image

    def show_trailer(self):
        """
        Shows a movies trailer in a browser.
        """
        webbrowser.open(self.youtube_trailer_url)