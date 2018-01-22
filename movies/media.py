import webbrowser

class Movie():
    """ This class provides a way to store movie realted information."""

    if __name__ == '__main__':
        print('This program is being run by itself')
    else:
        print('I am being imported from another module')

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
