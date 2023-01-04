"""
Screen class serves as base class for WelcomeScreen and UIScreen, and contains methods for
basic screen functionality.

    A Screen can be activated and deactivated, create buttons, draw itself, and
    handle events.
"""

import pygwidgets
import pygame

class Screen():

    def activate(self):
        """ Switches the isActive boolean to False to indicate the UIScreen object should
        be drawn. """
        self.isActive = True

    def createButton(self, button_label):
        """ Creates a button to be displayed on the screen. """
        self.button = pygwidgets.TextButton(self.window, (self.button_x, self.button_y),
                                            button_label.title(), width=self.button_width,
                                            height=self.button_height,
                                            nickname=button_label, fontSize=35)
        return self.button

    def deactivate(self):
        """ Switches the isActive boolean to False to indicate the WelcomeScreen object
        should not be drawn, and disables all menu buttons. """
        self.isActive = False
        for button in self.button_list:
            button.disable()

    def draw(self):
        """ Tells the screen's objects to draw themselves. """
        self.image.draw()
        for button in self.button_list:
            button.draw()

    def getIsActive(self):
        """ Returns boolean indicating whether or not the UI screen is active. """
        return self.isActive

    def handleEvent(self, event):
        """ Updates buttons based on mouse movement and sends out signals that buttons
        have been pressed.
        """
        for button in self.button_list:
            if button.handleEvent(event):
                return button.getNickname()
