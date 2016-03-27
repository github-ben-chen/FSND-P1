# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 20:32:03 2015

This script contains a list of movie objects, which are populated by fresh_tomatoes.py to a html file

"""

import media
import fresh_tomatoes


toy_story= media.Movie("Toy Story",
                       "A story of a boy and his torys that come to life",
                       "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v7_aa.jpg",
                       "https://www.youtube.com/watch?v=4KPTXpQehio")
                       
gravity   = media.Movie("Gravity",
                       "A medical engineer and an astronaut work together to survive after a catastrophe destroys their shuttle and leaves them adrift in orbit.",
                       "http://hashem.com/wp-content/uploads/sites/5/2015/04/13.jpg",
                       "https://www.youtube.com/watch?v=OiTiKOy59o4")
                       
avatar   = media.Movie("Avatar",
                       "A marien on an alien planet",
                       "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SX640_SY720_.jpg",
                       "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
                       
crouchingTiger  = media.Movie("Crouching Tiger, Hidden Dragon",
                       "Two warriors in pursuit of a stolen sword and a notorious fugitive are led to an impetuous, physically skilled, adolescent nobleman's daughter, who is at a crossroads in her life.",
                       "http://ia.media-imdb.com/images/M/MV5BMTY5MjM4NjIxOF5BMl5BanBnXkFtZTcwNDg5NzU2OQ@@._V1_SX640_SY720_.jpg",
                       "https://www.youtube.com/watch?v=oEaGsdiA0y0")
                       
iceAge   = media.Movie("Ice Age",
                       "Set during the Ice Age, a sabertooth tiger, a sloth, and a wooly mammoth find a lost human infant, and they try to return him to his tribe.",
                       "http://ia.media-imdb.com/images/M/MV5BMjEyNzI1ODA0MF5BMl5BanBnXkFtZTYwODIxODY3._V1_SX640_SY720_.jpg",
                       "https://www.youtube.com/watch?v=cMfeWyVBidk")

ExMachina   = media.Movie("Ex Machina",
                       "A young programmer is selected to participate in a breakthrough experiment in artificial intelligence by evaluating the human qualities of a breathtaking female A.I.",
                       "http://ia.media-imdb.com/images/M/MV5BMTUxNzc0OTIxMV5BMl5BanBnXkFtZTgwNDI3NzU2NDE@._V1_SX214_AL_.jpg",
                       "https://www.youtube.com/watch?v=XYGzRB4Pnq8")

movies = [iceAge, gravity,toy_story, crouchingTiger,avatar,ExMachina]
fresh_tomatoes.open_movies_page(movies)
