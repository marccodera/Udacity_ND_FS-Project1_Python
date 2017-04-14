import webbrowser

# Class Movie declares the data structure and functions for movies to be displayed
class Movie():
    """ Declares the data structure and functions for movies to be displayed.

    Functions:
        __init__(): Constructor that fills Movie variables
        show_trailer(): Opens the YouTube URL to show the trailer
    """

    # Constructor of the class, declared here with all of the properties
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """ Constructor that fills Movie variables with the data given while
            calling it.

        Variables:
            title (str): The Movie title given by movie_title
            storyline (str): The Movie storyline given by movie_storyline
            poster_image_url (str): The Movie poster image given by poster_image
            trailer_youtube_url (str): YouTube trailer URL set by trailer_youtube
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Function to show the Movie trailer, only uses self to get the URL for it
    def show_trailer(self):
        """ It opens the trailer of the movie on the page in the webbrowser """
        # This is a function from the webbrowser Python Module
        # it opens the movie trailer URL inside the browser
        webbrowser.open(self.trailer_youtube_url)
