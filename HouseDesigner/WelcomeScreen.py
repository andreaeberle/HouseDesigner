"""
WelcomeScreen class for an object that contains and manages information about the
welcome menu buttons.

    WelcomeScreen class inherits from the Screen base class.

    When the user clicks on one of the two buttons contained in the WelcomeScreen, that
    information is passed along to the GameController object.
"""

import pygwidgets
import pygame
from Screen import *

class WelcomeScreen(Screen):

    def __init__(self, window, window_width, window_height):
        self.window = window
        self.window_width = window_width
        self.window_height = window_height
        
        self.isActive = True # Boolean tracks whether or not the welcome screen
                                # should be displayed
        self.image = pygwidgets.Image(window, (0, 0),
                                      'images/welcome_screen.png')

        # Setting position of welcome screen in the center of the game window
        screenRect = self.image.getRect()
        self.width, self.height = screenRect[2:4]
        self.x = (self.window_width - self.width) / 2
        self.y = (self.window_height - self.height) / 2
        self.image.setLoc((self.x, self.y))

        # Creating menu buttons
        self.button_width = 300
        self.button_height = 100
        SPACE_BTWN_BUTTONS = 50
        self.button_x = 0
        self.button_y = 0
        
        self.button_list = [] # List to contain all welcome menu buttons
        self.buildHouseButton = self.createButton("build house")
        self.button_list.append(self.buildHouseButton)
        self.quitButton = self.createButton("quit")
        self.button_list.append(self.quitButton)

        # Setting position of menu buttons
        num_buttons = len(self.button_list)
        screen_edge_offset = ((self.width - (self.button_width * num_buttons) - (SPACE_BTWN_BUTTONS * (num_buttons - 1))) / 2) + self.x
        button_y = (self.height / 2) + self.y
        for button in self.button_list:
            button.setLoc((screen_edge_offset, button_y))
            screen_edge_offset += (self.button_width + SPACE_BTWN_BUTTONS)

