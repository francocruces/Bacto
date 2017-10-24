"""
Map.
"""

import numpy as np
from GUI.Point import Point
from GUI.GraphicColony import GraphicColony
from GUI.GraphicObject import AbstractGraphicObject
from GUI.GraphicSelect import GraphicSelect
from GUI.GraphicSelect import Hover
from GUI.GraphicParty import BackgroundParty
from GUI.InScreenClock import InScreenClock
from Settings.GUISettings import *
from Settings.GeneralSettings import *


class Map:
    """
    A wrapper for all current graphic objects. Updates them and draws them.
    """
    def __init__(self, width, height):
        """
        Constructor
        :type width: int
        :type height: int 
        """
        self.width = width
        self.height = height

        self.graphic_colonies = []
        self.graphic_parties = []
        self.selection = []
        self.hover = []
        self.background = []
        self.clock = InScreenClock(self, Point(self.width // 2, 0))

        self.mouse_position = Point(0, 0)

        self.is_over = False

    def empty(self):
        """
        Empty map
        """
        self.clock.reset()
        self.graphic_colonies = []
        self.graphic_parties = []
        self.selection = []
        self.hover = []
        self.mouse_position = Point(0, 0)

    def insert_graphic_colony(self, graphic_colony):
        """
        Insert a graphic object in corresponding array. 
        """
        self.graphic_colonies.append(graphic_colony)

    def insert_graphic_party(self, graphic_party):
        """
        Insert a graphic object in corresponding array. 
        """
        self.graphic_parties.append(graphic_party)

    def insert_selection(self, a_selection):
        """
        Insert a graphic object in corresponding array. 
        """
        self.selection.append(a_selection)

    def insert_hover(self, a_hover):
        """
        Insert a graphic object in corresponding array. 
        """
        self.hover.append(a_hover)

    def insert_background(self, background):
        """
        Insert a graphic object in corresponding array. 
        """
        self.background.append(background)

    def tick_background(self):
        """
        Tick background. This is meant to be independent from the rest of the objects.  
        """
        self.generate_background()
        for b in self.background:
            b.tick()

    def generate_background(self):
        """
        Generate new background objects if there aren't enough.
        """
        if len(self.background) < MAX_BACKGROUND_ELEMENTS:
            rad = np.random.randint(0, MAX_BACKGROUND_SIZE)
            pos_i = Point(0, 0)
            pos_f = Point(0, 0)
            side_i = np.random.randint(0, 3)
            side_f = np.random.randint(0, 3)
            if side_i == 0:  # Left side
                pos_i = Point(-rad, np.random.randint(0, SCREEN_HEIGHT))
            if side_i == 1:  # Right side
                pos_i = Point(SCREEN_WIDTH + rad, np.random.randint(0, SCREEN_HEIGHT))
            if side_i == 2:  # Upper side
                pos_i = Point(np.random.randint(0, SCREEN_WIDTH), -rad)
            if side_i == 3:  # Bottom side
                pos_i = Point(np.random.randint(0, SCREEN_WIDTH), SCREEN_HEIGHT + rad)

            if side_f == 0:  # Left side
                pos_f = Point(-rad, np.random.randint(0, SCREEN_WIDTH))
            if side_f == 1:  # Right side
                pos_f = Point(SCREEN_WIDTH + rad, np.random.randint(0, SCREEN_HEIGHT))
            if side_f == 2:  # Upper side
                pos_f = Point(np.random.randint(0, SCREEN_WIDTH), -rad)
            if side_f == 3:  # Bottom side
                pos_f = Point(np.random.randint(0, SCREEN_WIDTH), SCREEN_HEIGHT + rad)

            speed = np.random.rand(1) * MAX_BACKGROUND_SPEED * 7 / 10 + MAX_BACKGROUND_SPEED * 3 / 10
            BackgroundParty(self, pos_i, pos_f, rad, speed)

    def draw_background(self, surface):
        """
        Draw background on given surface.
        """
        for b in self.background:
            b.draw(surface)

    def tick(self):
        """
        Tick everything that's not background.
        :return: 
        """
        self.clock.tick()
        self.create_hovers()
        for p in self.graphic_parties:
            p.reset_ext_forces()
        self.check_collisions()

        self.tick_array(self.graphic_colonies)
        self.tick_array(self.graphic_parties)
        self.tick_array(self.selection)
        self.tick_array(self.hover)

    def draw(self, surface):
        """
        Draw everything that's not background.
        """
        self.draw_array(self.graphic_parties, surface)
        self.draw_array(self.graphic_colonies, surface)
        self.draw_array(self.selection, surface)
        self.draw_array(self.hover, surface)
        self.clock.draw(surface)

    @staticmethod
    def tick_array(array):
        """
        Tick given array.
        """
        for item in array:
            item.tick()

    @staticmethod
    def draw_array(array, surface):
        """
        Draw given array on given surface.
        """
        for item in array:
            item.draw(surface)

    def check_collisions(self):
        """
        Collide parties with colonies. 
        """
        for c in self.graphic_colonies:
            for p in self.graphic_parties:
                self.collision(p, c)

    def remove(self, o):
        """
        Remove object from map. Try every array.
        """
        try:
            self.graphic_colonies.remove(o)
        except ValueError:
            pass
        try:
            self.graphic_parties.remove(o)
        except ValueError:
            pass
        try:
            self.selection.remove(o)
        except ValueError:
            pass
        try:
            self.hover.remove(o)
        except ValueError:
            pass
        try:
            self.background.remove(o)
        except ValueError:
            pass

    @staticmethod
    def collision(gobj1, gobj2):
        """
        Collide two graphic objects. 
        :type gobj1: AbstractGraphicObject
        :type gobj2: AbstractGraphicObject
        """
        if gobj1.position.distance(gobj2.position) < (gobj1.hitbox + gobj2.hitbox):
            gobj1.collide(gobj2)
            gobj2.collide(gobj1)

    def get_colonies_in(self, position):
        """
        :type position: Point
        :return: Array with colonies containing given point 
        """
        result = []
        for c in self.graphic_colonies:
            if c.contains(position):
                result.append(c)
        return result

    def clear_selection(self):
        """
        Clear selection.
        """
        self.selection = []
        self.hover = []

    def send_to(self, gr_col, race):
        """
        Send parties from selection to given graphic colony. 
        :param gr_col: Destination
        :type gr_col: GraphicColony
        :param race: Race of the player making the move
        :type race: AbstractRace
        :return: 
        """
        for sel in self.selection:
            if not (sel.gr_colony == gr_col):
                if sel.gr_colony.get_race().same_type(race):
                    sel.gr_colony.send_party(gr_col)

    def select(self, gr_col, race):
        """
        Add colony to selection if it doesn't exceed selection limit and belongs to the player selecting.
        :param gr_col: GraphicColony to add
        :type gr_col: GraphicColony
        :param race: Race of the player perfoming selection
        :type race: AbstractRace
        """
        if len(self.selection) < MAX_SELECT_AMOUNT:
            if not self.is_selected(gr_col):
                if gr_col.colony.race.same_type(race):
                    return GraphicSelect(self, gr_col)

    def is_selected(self, gr_col):
        """ 
        :return: True if GraphicColony is selected, False otherwise.
        """
        for sel in self.selection:
            if sel.gr_colony == gr_col:
                return True
        return False

    def update_mouse_position(self, position):
        """
        Update mouse position
        :type position: Point 
        """
        self.mouse_position = position

    def create_hovers(self):
        """
        Hover with given mouse position.
        """
        colonies = self.get_colonies_in(self.mouse_position)
        self.hover = []
        for c in colonies:
            if not self.is_hovered(c):
                Hover(self, c)

    def is_hovered(self, gr_col):
        """
        :return: True if GraphicColony is hovered, False otherwise. 
        """
        for h in self.hover:
            if h.gr_colony == gr_col:
                return True
        return False

    def can_place_colony(self, radius, position):
        """
        :return: True if can be placed at given position, False otherwise.
        """
        for c in self.graphic_colonies:
            if c.position.distance(position) < (radius + c.radius):
                return False
        return True
