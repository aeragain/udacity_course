import webbrowser
import video


# extend Video and add movie variable
class Movie(video.Video):
    """Class describing attributes of a Movie.
       Extend Video class include title and duration.
    Note:
        Do not include the `self` parameter in the ``Args`` section.
    Args:
        title (str): Movie's title.
        duration (int): Movie's duration.
        movie_storyline (str): Movie's storyline.
        poster_image (str): Movie's poster image url.
        trailer_youtube (str): Movie's youtube trailer url.
    Methods:
        show_trailer (): open the trailer of the specified youtube url.
    """
    def __init__(self, title, duration, movie_storyline, poster_image,
                 trailer_youtube):
        video.Video.__init__(self, title, duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """open the trailer of the specified youtube url.

        Returns:
        None.
        """
        webbrowser.open(self.trailer_youtube_url)
