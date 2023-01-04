"""
HouseComponent class serves as the base class for all the seperately customizable components
of the house.

    Contains methods for basic functionalities required for all HouseComponent subclasses,
    such as building, drawing, updating, and finalizing themselves.

    Also initializes variables containing basic information about each HouseComponent:
    self.options, which contains the strings to be displayed on the UIScreen, describing
    the different image options available for each HouseComponent; self.under_construction,
    a boolean that indicates whether the HouseComponent is currently being customized by
    the user; and self.finalized, a boolean that indicates whether the user has finalized
    their choice for the HouseComponent's appearance.
"""

import pygwidgets
import pygame

class HouseComponent():

    def __init__(self):
        self.options = list(self.image_options.keys())
        self.under_construction = False
        self.finalized = False

    def build(self):
        """ Tells the HouseComponent that the user is starting to work on customizing it,
        and returns a string that should display to let the user know what component
        they're cutomizing and a list of options for the UIScreen to display to the user
        via buttons """
        self.under_construction = True
        return self.user_prompt, self.options[:-1]

    def draw(self):
        """ Tells the HouseComponent to draw itself """
        self.image.draw()

    def finalize(self):
        """ Tells the HouseComponent that the user has indicated they have finalized their
        choice for the HouseComponent's appearance """
        self.under_construction = False
        self.finalized = True

    def getFinalized(self):
        """ Returns the boolean self.finalized, indicating whether the user has finalized
        the appearance of the HouseComponent """
        return self.finalized

    def getUnderConstruction(self):
        """ Returns the boolean self.under_construction, indicating whether the user is
        currently working on customizing the HouseComponent """
        return self.under_construction

    def reset(self):
        """ Function is called if the user wishes to start building a new house. Removes
        the current image for the HouseComponent and resets the self.under_construction and
        self.finalized booleans to False """
        self.under_construction = False
        self.finalized = False
        self.image.replace("no_selection")

    def update(self, option):
        """ When the user selects an appearance option for a HouseComponent via the
        UIScreen, that option is passed through this function, which tells the
        HouseComponent to display the appropriate image for the user's selection """
        if option == "confirm":
            self.finalize()
        else:
            self.image.replace(option)
