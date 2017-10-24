"""
Graphic select.
"""

import pygame
import pygame.gfxdraw
from GUI.GraphicObject import AbstractGraphicObject
from Settings.GUISettings import *
import numpy as np


class GraphicSelect(AbstractGraphicObject):
    """
    An animated circle to show current selection.
    """
    def __init__(self, a_map, gr_colony):
        """
        Constructor.
        :type a_map: Map 
        :type gr_colony: GraphicColony
        """
        super(GraphicSelect, self).__init__(a_map, gr_colony.position, gr_colony.radius)
        self.gr_colony = gr_colony
        self.anim_radius = 0
        self.anim_time = 0

    def tick(self):
        """
        Update radius.
        """
        self.anim_time += 1
        self.anim_radius = (np.cos(self.anim_time / (np.pi * 2 * self.get_total_anim_time())) + 1) * self.get_anim_amp()

    def collide(self, o):
        """
        Collide with given object.
        """
        pass

    def add_to_map(self):
        """
        Add to its map.
        """
        self.map.insert_selection(self)

    def draw(self, surface):
        """
        Draw on given surface.
        :type surface: Surface
        """
        pygame.draw.circle(surface, self.get_color(), self.position.discretize().to_tuple(),
                           int(np.floor(self.radius + self.anim_radius)), self.get_width())
        pygame.draw.line(surface, self.get_color(), self.position.discretize().to_tuple(),
                         self.map.mouse_position.to_tuple(), self.get_line_width())

    def get_color(self):
        """
        :return: Color 
        """
        return THECOLORS['black']

    @staticmethod
    def get_width():
        """
        :return: Circle width
        """
        return SELECT_WIDTH

    @staticmethod
    def get_line_width():
        """
        :return: Line width
        """
        return SELECT_LINE_WIDTH

    @staticmethod
    def get_total_anim_time():
        """
        :return: Total animation time
        """
        return SELECT_ANIMATION_TIME

    def get_anim_amp(self):
        """
        :return: Animation amplitude
        """
        return SELECT_ANIMATION_AMP


class Hover(GraphicSelect):
    """
    Circle for hovering colonies.
    """
    def __init__(self, a_map, gr_colony):
        super(Hover, self).__init__(a_map, gr_colony)

    def get_anim_amp(self):
        """
        :return: Animation amplitude 
        """
        return 0

    def get_color(self):
        """
        :return: Color 
        """
        return THECOLORS['gray50']

    def draw(self, surface):
        """
        Draw on given surface.
        :type surface: Surface
        """
        pygame.draw.circle(surface, self.get_color(),
                           self.position.discretize().to_tuple(),
                           int(self.radius + self.anim_radius + HOVER_AMP),
                           self.get_width())

    def add_to_map(self):
        """
        Add to its map
        """
        self.map.insert_hover(self)
