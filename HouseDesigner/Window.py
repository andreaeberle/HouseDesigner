"""
Window class is a subclass of HouseComponent.

    Stores the image for the windows of the house. Allows for the instantiation of a "big"
    or "small" Window object
"""

import pygwidgets
import pygame
from HouseComponent import *

class Window(HouseComponent):

    def __init__(self, window, house_x, house_y, house_width, size):
        self.window = window
        
        # Setting the text that will prompt the user to make a selection of
        # window shape type
        user_prompt_big = "Pick a shape for the \nwindows of your house:"
        user_prompt_small = "Pick a shape for the \naccent windows of \nyour house:"
        
        # Initializing image details
        self.image_options = {"square" : "images/square_window.png",
                        "circle" : "images/circle_window.png",
                        "triangle" : "images/triangle_window.png",
                        "no_selection" : "images/void_image.png"}
        self.image = pygwidgets.ImageCollection(window, (0, 0), self.image_options,
                                                "no_selection")

        # Setting location based on whether the big or small window is being intantiated
        if size == "big":
            self.x = house_x + (house_width * 0.57)
            self.y = house_y + 190
            self.user_prompt = user_prompt_big
        else:
            self.image.scale(66, scaleFromCenter=False)
            self.x = house_x + (house_width * 0.41)
            self.y = house_y + 70
            self.user_prompt = user_prompt_small
        self.image.setLoc((self.x, self.y))

        HouseComponent.__init__(self)
