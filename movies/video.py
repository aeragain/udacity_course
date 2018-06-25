# The parent class include title and duration
class Video():
    """Class describing attributes of a Movie.
    Note:
        Do not include the `self` parameter in the ``Args`` section.
    Args:
        title (str): Videos's title.
        duration (int): Videos's duration.
    """
    def __init__(self, title, duration):
        print("Parent constructor called")
        self.title = title
        self.duration = duration
