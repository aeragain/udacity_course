import webbrowser
import video


# extend Video and add movie variable
class Movie(video.Video):
    """Class describing attributes of a Movie.
    """
    def __init__(self, title, duration, movie_storyline, poster_image,
                 trailer_youtube):
        video.Video.__init__(self, title, duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """open the trailer of the specified youtube url.
        """
        webbrowser.open(self.trailer_youtube_url)
