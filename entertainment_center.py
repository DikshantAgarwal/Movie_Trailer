import media
import fresh_tomatoes
"""These are different instance of class Movie like:-
    1.toy_story
    2.Avatar
    3.Znmd
    4.iqbal
    5.lakshya
    6.pursuit_of_happiness
"""
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toy that come into life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie(
    "Avatar",
    "A marine in alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")
pursuit_of_happiness = media.Movie(
    "Pursuit of happines",
    "A story of struggle of a common man",
    "http://www.impawards.com/2006/posters/pursuit_of_happyness.jpg",
    "https://www.youtube.com/watch?v=89Kq8SDyvfg")
znmd = media.Movie(
    "Zindagi Na Milegi Dobara",
    "The trip turns into an opportunity to mend fences, heal wounds, fall in l"
    "ove with life and combat their worst fears",
    "https://s-media-cache-ak0.pinimg.com/736x/70/c0/b7/70c0b79448a34da436fab4"
    "16212f0746.jpg",
    "https://www.youtube.com/watch?v=lAuJoq6zeIQ")
lakshya = media.Movie(
    "Lakshya",
    "Coming-of-age tale of out-of-college drifter Karan who joins the army on i"
    "mpulse but must face up to its challenges to prove himself to the woman h"
    "e loves", "http://www.impawards.com/intl/india/2004/posters/lakshya.jpg",
    "https://www.youtube.com/watch?v=YoKGmYyljmc")
iqbal = media.Movie(
    "Iqbal",
    "Iqbal, a deaf and mute boy, only dreams of making it into the Indian cric"
    "ket team. His status hinders his selection, and he picks a retired coach"
    "to train him, who leads him to his dream.",
    "https://upload.wikimedia.org/wikipedia/en/a/ad/Iqbal_poster.jpg",
    "https://www.youtube.com/watch?v=VbEISCo8FKA")
# An array of movie which is passed to fresh_tomato python file
movies = [toy_story, avatar, pursuit_of_happiness, znmd, lakshya, iqbal]
fresh_tomatoes.open_movies_page(movies) # An array is passed as argument 

