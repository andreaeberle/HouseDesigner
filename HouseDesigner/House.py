"""
House class creates all necessary objects from the HouseComponent subclasses, sends messages
to relevant HouseComponents when appropriate, and contains some basic information about
where the house should be located in the game window, so that all HouseComponents can set
their locations accordingly.

    Receives information from the UIScreen via the GameController when a HouseComponent's
    image needs to be updated, and passes that information along to the appropriate
    component to update themselves.

"""

import pygwidgets
import pygame
from Base import *
from Roof import *
from Window import *
from Tree import *

class House():

    def __init__(self, window, window_width, window_height):
        self.window = window
        self.components = []
        self.window_width = window_width
        self.window_height = window_height
        self.WIDTH = 344

        # Setting location of the house
        self.x = self.window_width * 0.63
        self.y = self.window_height * 0.20

        self.finished = False # Boolean tracks whether or not house is finished

        # Initializing all house components in the order the user should be asked
        # to create them
        self.oBase = Base(window, self.x, self.y)
        self.components.append(self.oBase)
        self.oRoof = Roof(window, self.x, self.y)
        self.components.append(self.oRoof)
        self.oBigWindow = Window(window, self.x, self.y, self.WIDTH, "big")
        self.components.append(self.oBigWindow)
        self.oSmallWindow = Window(window, self.x, self.y, self.WIDTH, "small")
        self.components.append(self.oSmallWindow)
        self.oTree = Tree(window, self.x, self.y)
        self.components.append(self.oTree)

    def buildComponent(self):
        """ Creates an object for each component of the house """
        for component in self.components:
            if not component.getFinalized(): # Finds the next unfinalized component
                if component.__str__() == "Roof": # Ensures the roof object is drawn behind
                                                # all other house components
                    index = self.components.index(component)
                    self.components.insert(0, self.components.pop(index))
                return component.build()
        self.finished = True # Indicates house has been finished

    def draw(self):
        """ Tells all house components to draw themselves """
        for component in self.components:
            component.draw()

    def getFinished(self):
        """ Returns the boolean self.finished, indicating whether or not all house
        components have been built """
        return self.finished

    def reset(self):
        """ Clears all house components and returns the house object to its
        stsrting state """
        self.finished = False

        # Ensuring the roof object is the second house component presented to the user
        for component in self.components:
            if component.__str__() == "Roof": 
                index = self.components.index(component)
                self.components.insert(1, self.components.pop(index))

        # Reseting all components
        for component in self.components:
            component.reset()

    def updateComponents(self, option):
        """ Tells the appropriate house component to update itself """
        for component in self.components:
            if component.getUnderConstruction():
                component.update(option)
                
