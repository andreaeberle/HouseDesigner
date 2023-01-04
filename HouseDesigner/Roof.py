"""
Roof class is a subclass of HouseComponent.

    Stores the image for the roof of the house. Contains a method overriding
    the __str__ method so that the House object can adjust the roof's drawing
    order.
"""

import pygwidgets
import pygame
from HouseComponent import *

class Roof(HouseComponent):

    def __init__(self, window, house_x, house_y):
        self.window = window
        self.x = house_x
        self.y = house_y

        # Setting the text that will prompt the user to make a selection of roof type
        self.user_prompt = "Pick a color for the roof \nof your house:"

        # Initializing image details
        self.image_options = {"black" : "images/black_roof.png",
                        "blue" : "images/blue_roof.png",
                        "brown" : "images/brown_roof.png",
                        "no_selection" : "images/void_image.png"}
        self.image = pygwidgets.ImageCollection(window, (self.x, self.y), self.image_options,
                                                "no_selection")
        HouseComponent.__init__(self)

    def __str__(self):
        return "Roof"
