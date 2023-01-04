"""
GameController class is designed to instantiate an object that maintains primary
responsibility for passing messages to the various game modules.

    Initializes the game's aggregating objects: WelcomeScreen, UIScreen, and House. Holds
    responsibility for transitioning the game through its different stages: launching the
    welcome screen, building the house, and launching the end screen.

    Acts as an intermediary between the UIScreen and the House, passing any selections the
    user makes via buttons on the UIScreen to the House, which in turn distills the
    information to prompt the appropriate action from the relevant object of a
    HouseComponent subclass.
"""

import pygwidgets
import pygame
from WelcomeScreen import *
from UIScreen import *
from House import *

class GameController():

    def __init__(self, window, window_width, window_height):
        self.window = window
        self.window_width = window_width
        self.window_height = window_height

        # Initializing game's aggregating objects
        self.screen_list = [] # List contains all screen objects
        self.oWelcomeScreen = WelcomeScreen(window, self.window_width, self.window_height)
        self.screen_list.append(self.oWelcomeScreen)
        self.oUIScreen = UIScreen(window, self.window_width, self.window_height)
        self.screen_list.append(self.oUIScreen)
        self.oHouse = House(window, self.window_width, self.window_height)

    def handleEvent(self, event):
        """ Passes game event to any active screens.
        """
        for screen in self.screen_list:
            if screen.getIsActive():
                screen_message = screen.handleEvent(event)
                if screen_message == "quit":
                    return "quit"
                elif screen_message == "build house":
                    #Shifting to UI screen and starting house building portion of game
                    self.oWelcomeScreen.deactivate()
                    self.oUIScreen.activate()
                    self.oUIScreen.presentChoice(self.oHouse.buildComponent())
                elif screen_message == "build new house":
                    self.oHouse.reset()
                    self.oUIScreen.presentChoice(self.oHouse.buildComponent())
                elif screen_message == "confirm":
                    self.oHouse.updateComponents(screen_message)
                    try:
                        self.oUIScreen.presentChoice(self.oHouse.buildComponent())
                    except TypeError: # Exception is thrown when there are no more
                                    # components left to build
                        self.oUIScreen.displayEndScreen()
                elif screen_message:
                    self.oHouse.updateComponents(screen_message)

    def draw(self):
        """ Calls appropriate methods to draw all active elements in the
        game window.
        """
        for screen in self.screen_list:
            if screen.getIsActive():
                screen.draw()

        self.oHouse.draw()
