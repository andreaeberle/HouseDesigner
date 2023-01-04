"""
The main script for the game "House Design Simulator."

    Initializes game window, GameController, and the game's static background image.
    Processes quit requests, controls the game's frame rate, and prompts the GameController
    to handle events and draw screen elements with each new frame.
"""

import pygame
from pygame.locals import *
import sys
import pygwidgets
from GameController import *

# Establishing constants
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
FRAMES_PER_SECOND = 30

# Initializing window and time-keeping
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Initializing background image
backgroundImage = pygwidgets.Image(window, (0, 0), 'images/background.png')

# Initializing game controller object
oGameController = GameController(window, WINDOW_WIDTH, WINDOW_HEIGHT)

# Main Loop
while True:

    # Event checking and handling
    for event in pygame.event.get():

        # User clicks on window's "X" quit button
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if oGameController.handleEvent(event) == "quit":
            pygame.quit()
            sys.exit()

    # Clearing the screen
    backgroundImage.draw()

    # Drawing all on-screen elements
    oGameController.draw()

    # Updating window
    pygame.display.update()

    # Slowing down processing to appropriate frames per second
    clock.tick(FRAMES_PER_SECOND)
