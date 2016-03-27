# -*- coding: utf-8 -*-
"""
This class defines a data structure for movie entry, including the following info
1. title
2. story_line
3. poster_url
4. trailer_url

"""
import webbrowser

class Movie:
    def __init__(self, movie_title, movie_storyline,poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    
    def show_trailder(self):
        webbrowser.open(self.trailer_youtube_url)
