"""
Event handler class.
"""

import pygame
import pygame.mixer
from pygame.locals import *
from Settings import KeySettings


class EventHandler:
    """
    Handles input.
    """
    def __init__(self, driver):
        """
        Constructor.
        :param driver: Driver to control
        """
        self.driver = driver
        self.mouse_held = False

    def handle_events(self):
        """
        Handle input and control driver accordingly
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.driver.quit()
            if event.type == pygame.MOUSEMOTION:
                self.driver.update_mouse_position(event.pos)
            if event.type == pygame.MOUSEBUTTONUP and self.mouse_held:
                self.mouse_held = False
                self.driver.release_mouse(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_held = True
            if event.type == pygame.MOUSEMOTION:
                if self.mouse_held:
                    self.driver.select(event.pos)
                else:
                    self.driver.hover(event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == KeySettings.PAUSE:
                    self.driver.pause_key()
                if event.key == KeySettings.MAIN_MENU:
                    self.driver.main_menu_key()
                if event.key == KeySettings.SELECTION_LEFT:
                    self.driver.selection_left()
                if event.key == KeySettings.SELECTION_RIGHT:
                    self.driver.selection_right()
                if event.key == KeySettings.SELECTION_DOWN:
                    self.driver.selection_down()
                if event.key == KeySettings.SELECTION_UP:
                    self.driver.selection_up()
                if event.key == K_RETURN or event.key == K_SPACE:
                    self.driver.select_key()
