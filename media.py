import webbrowser

"""This is a python class(data structure) having:- 
    
    1.Favorite movies
    2.Movie title
    3.Box art URL (or poster URL)
    4.YouTube link to the movie trailer.
    
    
    """
class Movie():
    def __init__(
            self,
            movie_title,
            movie_storyline,
            poster_image,
            trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
# instance method to open the youtube link of movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)



