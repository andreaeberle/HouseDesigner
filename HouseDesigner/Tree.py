"""
Tree class is a subclass of HouseComponent.

    Stores the image for the tree next to the house.
"""

import pygwidgets
import pygame
from HouseComponent import *

class Tree(HouseComponent):

    def __init__(self, window, house_x, house_y):
        self.window = window
        self.x = house_x - 235
        self.y = house_y
        
        # Setting the text that will prompt the user to make a selection of base type
        self.user_prompt = "Pick a tree to plant \nby your house:"

        # Initializing image details
        self.image_options = {"maple" : "images/maple_tree.png",
                        "pine" : "images/pine_tree.png",
                        "cherry" : "images/cherry_tree.png",
                        "no_selection" : "images/void_image.png"}
        self.image = pygwidgets.ImageCollection(window, (self.x, self.y), self.image_options,
                                                "no_selection")

        HouseComponent.__init__(self)
