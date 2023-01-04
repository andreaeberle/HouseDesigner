"""
UIScreen class for an object that contains and manages information about the buttons used
to construct the house.

    UIScreen class inherits from the Screen base class.

    UIScreen can be passed any number of options to display via buttons for the user. When
    the user clicks on one of these buttons, the UIScreen passes this information to the
    GameController object.
"""

import pygwidgets
import pygame
from Screen import *

class UIScreen(Screen):

    def __init__(self, window, window_width, window_height):
        self.window = window
        self.window_width = window_width
        self.window_height = window_height
        
        self.isActive = False # Boolean tracks whether or not the UI screen
                                # should be displayed
        self.image = pygwidgets.Image(window, (0, 0),
                                      'images/ui_screen.png')
        screen_rect = self.image.getRect()
        self.width = screen_rect[2]
        self.height = screen_rect[3]

        self.title_y = 40

        self.prompt_y = self.height * 0.16

        self.button_width = self.width * 0.75
        self.button_height = self.button_width / 3
        self.SPACE_BTWN_BUTTONS = 20

    def displayEndScreen(self):
        """ Calls the UIScreen method presentChoice(), passing in arguments to display the
        end game message and prompt the user to either quit or start building a new house """
        user_prompt = "You've built a fantastic \nhouse! \n\nWhat would you like to \ndo now?\n\n"
        options = ["build new house", "quit"]
        self.presentChoice((user_prompt, options), confirm_option=False,
                           title_display="Congratulations!")
    
    def draw(self):
        """ Expanding on base class' draw() method to display a prompt for the user. """
        Screen.draw(self)
        self.title_display.draw()
        self.prompt_display.draw()

    def handleEvent(self, event):
        """ Overriding base class' handleEvent() method to include special behavior for
        a confirm button.
        """
        if self.confirm_option:
            for button in self.button_list:
                if button.handleEvent(event):
                    if not self.confirm_button.getEnabled():
                        self.confirm_button.enable()
                    return button.getNickname()
        else:
            for button in self.button_list:
                if button.handleEvent(event):
                    return button.getNickname()

    def presentChoice(self, choice_info, confirm_option=True, title_display="Build Your House!"):
        """ Displays a prompt on UI screen that explains the choice the user is being asked
        to make, and populates the screen with a button for each option the user has. """
        user_prompt, options = choice_info
        self.confirm_option = confirm_option

        # Creating display for title
        self.title_display = pygwidgets.DisplayText(self.window, (0, self.title_y),
                                                     justified='center', value=title_display,
                                                     width=self.width, fontSize=55)

        # Creating display for prompt
        self.prompt_display = pygwidgets.DisplayText(self.window, (0, self.prompt_y),
                                                     justified='center', value=user_prompt,
                                                     width=self.width, fontSize=40)
        prompt_display_rect = self.prompt_display.getRect()
        prompt_height = prompt_display_rect[3]

        # Creating buttons and setting their locations
        self.button_list = []
        self.button_x = (self.width - self.button_width) / 2
        self.button_y = self.prompt_y + prompt_height + 25

        for option in options:
            self.createButton(option)
            self.button_y += (self.button_height + self.SPACE_BTWN_BUTTONS)
            self.button_list.append(self.button)

        # Creating an initially disabled confirm button
        if self.confirm_option:
            self.button_y = self.height - self.button_height - 40
            self.confirm_button = self.createButton("confirm")
            self.confirm_button.disable()
            self.button_list.append(self.confirm_button)
        
