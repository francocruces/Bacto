"""
Menu.
"""

from GUI.Point import Point
from GUI.Menu.MenuItem import *


class Menu:
    """
    Menu class. Represents a menu with labels and buttons. Animates and draws them.
    """
    def __init__(self, driver):
        """
        Constructor.
        :param driver: Current game driver. 
        """
        self.menu_items = []
        self.active_selection = 0
        self.mouse_position = Point(0, 0)
        self.driver = driver

    def insert_item(self, item):
        """
        Insert a menu item.
        :param item: Item to add
        :type item: MenuItem 
        """
        self.menu_items.append(item)

    def switch_menu(self, menu):
        """
        Switch to another given menu. State pattern.
        :param menu: Next menu 
        :type menu: Menu
        """
        self.driver.menu = menu

    def tick(self):
        """
        Update menu items and hovers.
        """
        for item in self.menu_items:
            item.tick()
        self.menu_items[self.active_selection].hover()

    def update_mouse_position(self, position):
        """
        Store current mouse position. Hovers.
        :param position: Mouse position
        :type position: Point
        """
        self.hover(position)

    def draw(self, surface):
        """
        Draw menu centered on the screen.
        :param surface: Surface to draw
        :type surface: Surface
        """
        v_size = self.get_vertical_size()
        center = Point(surface.get_size()[0], surface.get_size()[1]).scale(0.5)
        current_position = center - v_size.copy().scale(0.5)
        for item in self.menu_items:
            item.set_position(current_position.copy())
            current_position = current_position + Point(0, item.get_size().y).copy()
        for item in self.menu_items:
            item.draw(surface)

    def get_vertical_size(self):
        """
        Get vertical size of all the menu items stacked together.
        :return: Vertical size
        :rtype: Point
        """
        v_size = Point(0, 0)
        for item in self.menu_items:
            v_size.y += item.get_size().y
        return v_size

    def release_mouse(self, position):
        """
        Handle mouse release at given position
        :type position: Point 
        :return: 
        """
        self.select_items(self.get_menu_items_in(position))

    def hover(self, position):
        """
        Hover at given position.
        :type position: Point 
        """
        for item in self.get_menu_items_in(position):
            self.active_selection = self.menu_items.index(item)
            return  # Hover only once

    def selection_left(self):
        """
        Handle selection movement.
        """
        self.menu_items[self.active_selection].setting_left()
        self.driver.play_move_selection()

    def selection_right(self):
        """
        Handle selection movement.
        """
        self.menu_items[self.active_selection].setting_right()
        self.driver.play_move_selection()

    def selection_up(self):
        """
        Handle selection movement.
        """
        self.move_selection_up()
        while not self.menu_items[self.active_selection].is_selectable():
            self.move_selection_up()
        self.driver.play_move_selection()

    def selection_down(self):
        """
        Handle selection movement.
        """
        self.move_selection_down()
        while not self.menu_items[self.active_selection].is_selectable():
            self.move_selection_down()
        self.driver.play_move_selection()

    def move_selection_up(self):
        if self.active_selection == 0:
            self.active_selection = len(self.menu_items) - 1
        else:
            self.active_selection -= 1

    def move_selection_down(self):
        if self.active_selection == len(self.menu_items) - 1:
            self.active_selection = 0
        else:
            self.active_selection += 1

    def select_items(self, menu_items):
        """
        Select an array of menu items.
        :param menu_items: Array of menu items
        :type menu_items: list
        """
        for item in menu_items:
            item.select()
            self.driver.play_select()

    @staticmethod
    def hover_items(menu_items):
        """
        Hover an array of menu items.
        :param menu_items: Array of menu items
        :type menu_items: list
        """
        for item in menu_items:
            item.hover()

    def get_menu_items_in(self, position):
        """
        Get menu items containing given point.
        :param position: Point to scan
        :type position: Point
        :return: Menu items under position
        :rtype list
        """
        result = []
        for item in self.menu_items:
            if item.contains(position):
                result.append(item)
        return result

    def select_key(self):
        """
        Handle select key press.
        """
        self.menu_items[self.active_selection].select()
        self.driver.play_select()

    def set_selection(self, number):
        """
        Set selection to given number. Useful for proper initialization.
        :param number: Item to select (starts from 0)
        """
        self.active_selection = number
