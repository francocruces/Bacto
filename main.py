"""
Main. Run this
"""

import pygame
from Driver import Driver
from Settings.GeneralSettings import *
from Settings.GUISettings import *

pygame.init()

size = width, height = SCREEN_WIDTH, SCREEN_HEIGHT
game_screen = pygame.Surface(size)
text_screen = pygame.Surface(size)
background_screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bacto by Franco Cruces Ayala", "res/icon2.png")

game_screen.set_alpha(0)
text_screen.set_alpha(0)

clock = pygame.time.Clock()

gameExit = False

driver = Driver(game_screen, background_screen, text_screen)
null_color = THECOLORS['gray55']
while driver.is_running():
    clock.tick(GAME_TICKS_PER_SECOND)
    background_screen.fill(THECOLORS['gray80'])

    text_screen.fill(null_color)
    game_screen.fill(null_color)
    text_screen.set_colorkey(null_color)
    game_screen.set_colorkey(null_color)
    driver.tick()
    background_screen.blit(game_screen, (0, 0))
    background_screen.blit(text_screen, (0, 0))

    pygame.display.flip()
