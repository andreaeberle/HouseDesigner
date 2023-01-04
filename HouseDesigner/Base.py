"""
Base class is a subclass of HouseComponent.

    Stores the image for the walls of the house.
"""

import pygwidgets
import pygame
from HouseComponent import *

class Base(HouseComponent):

    def __init__(self, window, house_x, house_y):
        self.window = window
        self.x = house_x + 25
        self.y = house_y + 29

        # Setting the text that will prompt the user to make a selection of base type
        self.user_prompt = "Pick a color for the base \nof your house:"

        # Initializing image details
        self.image_options = {"yellow" : "images/yellow_base.png",
                        "green" : "images/green_base.png",
                        "red" : "images/red_base.png",
                        "no_selection" : "images/void_image.png"}
        self.image = pygwidgets.ImageCollection(window, (self.x, self.y), self.image_options,
                                                "no_selection")

        HouseComponent.__init__(self)
