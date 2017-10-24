"""
In screen clock
"""

from Settings.GeneralSettings import *
from GUI.Point import Point
import pygame
from Settings.GUISettings import *


class InScreenClock:
    """
    A clock to draw in a map.
    """
    def __init__(self, a_map, upper_center_point):
        """
        Constructor
        :type a_map: Map 
        :param upper_center_point: Upper center position of rectangular clock
        :type upper_center_point: Point
        """
        self.map = a_map
        self.ticks = 0
        self.time = 0
        self.upper_center_point = upper_center_point
        self.font = pygame.font.Font("res/Cabin-Bold.ttf", CLOCK_FONT_SIZE)

    def reset(self):
        """
        Set time to 0 
        """
        self.ticks = 0
        self.time = 0

    def time_as_text(self):
        """
        :return: Time as a text 
        """
        seconds = str(self.time % 60)
        minutes = str(self.time // 60)
        if len(seconds) == 1:
            seconds = "0" + str(seconds)
        if len(minutes) == 1:
            minutes = "0" + str(minutes)
        return minutes + ":" + seconds

    def tick(self):
        """
        Update time.
        """
        if not self.map.is_over:
            self.ticks += 1
            if self.ticks // GAME_TICKS_PER_SECOND > 0:
                self.ticks = 0
                self.time += 1

    def draw(self, surface):
        """
        Draw on given surface
        :type surface: Surface
        """
        label = self.font.render(self.time_as_text(), 1, CLOCK_TEXT_COLOR)
        text_max_size = Point(self.font.size("00:00")[0], self.font.size("00:00")[1])
        text_size = Point(self.font.size(self.time_as_text())[0], self.font.size(self.time_as_text())[1])
        top_left_corner = self.upper_center_point - Point(text_size.copy().scale(0.5).x, 0)
        p1 = (self.upper_center_point + Point(-text_max_size.copy().scale(0.5).x, 0)).to_tuple()
        p2 = (self.upper_center_point + Point(text_max_size.copy().scale(0.5).x, 0)).to_tuple()
        p3 = (self.upper_center_point + Point(text_max_size.copy().scale(0.5).x,
                                              text_max_size.copy().y)).to_tuple()
        p4 = (self.upper_center_point + Point(-text_max_size.copy().scale(0.5).x,
                                              text_max_size.copy().y)).to_tuple()

        pygame.draw.polygon(surface, CLOCK_RECT_COLOR, [p1, p2, p3, p4])
        surface.blit(label, top_left_corner.to_tuple())
