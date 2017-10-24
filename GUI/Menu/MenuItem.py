"""
Menu items.
"""

from GUI.Point import Point
import abc
import pygame
from GUI.Menu.MenuHandler import NullHandler
from Settings.GUISettings import *
from MapManager import NAME_FIELD


class MenuItem:
    """
    Menu item class. Represents an item in a menu. Implements common functionality.
    """

    def __init__(self, menu, handler, size=DEFAULT_FONT_SIZE, bold=False):
        """
        Constructor.
        :param menu: Underlying menu
        :param handler: Handler
        :param size: Font size
        :param bold: Flag to make bold
        :type bold: bool
        """
        self.text = ""
        self.menu = menu
        self.handler = handler
        self.font = pygame.font.Font("res/Cabin-Regular.ttf", size)
        self.font.set_bold(bold)
        self.position = Point(0, 0)

    def set_position(self, position):
        """
        Set position.
        :type position: Point 
        :return: 
        """
        self.position = position

    def handle(self):
        """
        Handle expected action.
        """
        self.handler.handle()

    def tick(self):
        """
        Update option. Meant to animate.
        """
        self.animate()

    @abc.abstractmethod
    def draw(self, surface):
        """
        Draw on given surface.
        :param surface: Surface to draw
        :type surface: Surface
        """
        pass

    def contains(self, position):
        """
        :type position: Point 
        :return: True if contains given position, False otherwise 
        """
        size = self.get_size().scale(0.5)
        ul = self.position - size
        br = self.position + size
        return ul.x < position.x < br.x and ul.y < position.y < br.y

    @abc.abstractmethod
    def select(self):
        """
        Select menu item
        """
        pass

    @abc.abstractmethod
    def hover(self):
        """
        Hover menu item.
        """
        pass

    @abc.abstractmethod
    def animate(self):
        """
        Animate menu item.
        """
        pass

    @abc.abstractmethod
    def get_size(self):
        """
        :return: Size
        :rtype: Point
        """
        pass

    def setting_left(self):
        """
        Handle horizontal movement. 
        """
        pass

    def setting_right(self):
        """
        Handle horizontal movement. 
        """
        pass

    @staticmethod
    def is_selectable():
        """        
        :return: True if can be selected, False otherwise 
        """
        return True


class Button(MenuItem):
    """
    A button. It is can be clicked.
    """

    def __init__(self, menu, handler, text):
        """
        Constructor.
        :param menu: Underlying menu
        :param handler: Handler
        :param text: Text
        """
        super(Button, self).__init__(menu, handler)
        self.text = text

    def tick(self):
        """
        Update item. Sets underline off (later turned back on if hovered)
        """
        self.font.set_underline(False)

    def hover(self):
        """
        Hover item. Currently set to underline text.
        """
        self.font.set_underline(True)

    def draw(self, surface):
        """
        Draw on given surface.
        :param surface: Surface to draw
        :type surface: Surface
        """
        label = self.font.render(self.text, 1, GUI_TEXT_COLOR)
        font_point = self.get_size().scale(0.5)
        surface.blit(label, (self.position - font_point).to_tuple())

    def animate(self):
        """
        Animate menu item.
        """
        pass

    def get_size(self):
        """
        :return: Size
        :rtype: Point
        """
        return Point(self.font.size(self.text)[0], self.font.size(self.text)[1])

    def select(self):
        """
        Handle. 
        """
        self.handler.handle()


class Label(MenuItem):
    """
    Just a text. Doesnt do anything else than drawing itself.
    """

    def __init__(self, menu, text, font_size=TITLE_FONT_SIZE, bold=False):
        """
        Constructor.
        :param menu: Unterlying menu
        :param text: Label
        :param font_size: Font size
        :param bold: Flag to make text bold
        """
        super(Label, self).__init__(menu, NullHandler(), font_size, bold)
        self.text = text
        self.size = Point(self.font.size(self.text)[0], self.font.size(self.text)[1])

    def tick(self):
        """
        On tick, do nothing
        """
        pass

    def hover(self):
        """
        On hover, do nothing
        """
        pass

    def contains(self, position):
        """
        Do nothing.
        """
        pass

    def draw(self, surface):
        """
        Draw on given surface.
        :param surface: Surface to draw
        :type surface: Surface
        """
        label = self.font.render(self.text, 1, GUI_TEXT_COLOR)
        font_point = self.get_size().scale(0.5)
        surface.blit(label, (self.position - font_point).to_tuple())

    def get_size(self):
        """
        :return: Size
        :rtype: Point
        """
        return Point(self.font.size(self.text)[0], self.font.size(self.text)[1])

    def animate(self):
        """
        Do nothing. 
        """
        pass

    def select(self):
        """
        On selection, do nothing
        """
        pass

    @staticmethod
    def is_selectable():
        """        
        :return: True if can be selected, False otherwise 
        """
        return False


class Setting(MenuItem):
    """
    A menu item. Changes game settings according to selected option.
    """

    def __init__(self, menu, handler, text):
        """
        Constructor
        :param menu: Underlying menu
        :param handler: Handler
        :param text: Label
        """
        super(Setting, self).__init__(menu, handler)
        self.options = []
        self.active_option = 0
        self.text = text

    def insert_option(self, option):
        """
        Insert an option.
        :param option: Option to add
        :type option: SettingOption
        """
        self.options.append(option)
        self.options[0].select()

    def tick(self):
        """
        Update item and options.
        """
        self.font.set_underline(False)
        for option in self.options:
            option.tick()

    def hover(self):
        """
        Hover item and options. 
        """
        self.font.set_underline(True)
        for option in self.options:
            option.hover()

    def draw(self, surface):
        """
        Draw on given surface.
        :param surface: Surface to draw
        :type surface: Surface
        """
        label = self.font.render(self.text, 1, GUI_TEXT_COLOR)
        font_point = self.get_size().scale(0.5)
        top_left_corner = self.position - font_point
        surface.blit(label, top_left_corner.to_tuple())
        self.options[self.active_option].draw(surface, self.position + Point(self.font.size(self.text)[0] / 2, 0))

    def get_size(self):
        """
        :return: Size
        :rtype: Point
        """
        return Point(self.font.size(self.text)[0], self.font.size(self.text)[1]) + Point(
            self.options[self.active_option].get_size().x, 0)

    def animate(self):
        """
        Do nothing.
        """
        pass

    def select(self):
        """
        On selection, change option. 
        """
        self.setting_right()

    def setting_left(self):
        """
        Move option to the left cyclically.
        """
        if self.active_option == 0:
            self.select_option(len(self.options) - 1)
        else:
            self.select_option(self.active_option - 1)

    def setting_right(self):
        """
        Move option to the right cyclically.
        """
        if self.active_option == len(self.options) - 1:
            self.select_option(0)
        else:
            self.select_option(self.active_option + 1)

    def select_option(self, index):
        """
        Select option. Useful for proper initialization.
        :param index: Option to select
        :type index: int
        """
        self.active_option = index
        self.options[self.active_option].select()


class SettingOption:
    """
    An option for a Setting menu item. 
    """

    def __init__(self, driver, parent):
        """
        Constructor.
        :param driver: Current game driver
        :param parent: Underlying menu item.
        :type parent: Setting
        """
        self.driver = driver
        self.font = pygame.font.Font("res/Cabin-Regular.ttf", DEFAULT_FONT_SIZE)
        self.parent = parent

    @abc.abstractmethod
    def select(self):
        """
        On selection, do nothing.
        """
        pass

    @abc.abstractmethod
    def get_size(self):
        """
        Doesn't have size yet.
        """
        pass

    @abc.abstractmethod
    def draw(self, surface, position):
        """
        Draw on given surface.
        :param surface: Surface to draw
        :type surface: Surface
        :param position: Position to draw
        :type position: Point
        """
        pass

    def tick(self):
        """
        Update. 
        """
        self.font.set_underline(False)

    def hover(self):
        """
        Hover. 
        """
        self.font.set_underline(True)

    def get_text(self):
        """
        Get text with self label.
        """
        return "[ " + str(self.get_label()) + " ]"

    @abc.abstractmethod
    def get_label(self):
        """
        Label to draw.
        """
        pass


class PlayerRaceOption(SettingOption):
    """
    Option for race setting.
    """

    def __init__(self, driver, parent, race):
        """
        Constructor.
        :param driver: Current game driver
        :type driver: Driver
        :param parent: Underlying menu item.
        :type parent: Setting
        :param race: Race for this option.
        """
        super(PlayerRaceOption, self).__init__(driver, parent)
        self.race = race

    def select(self):
        """
        Select option. Change settings accordingly.
        """
        self.driver.player_one.set_race(self.race)

    def get_size(self):
        """
        :return: Size
        :rtype: Point
        """
        return Point(self.font.size(self.get_text())[0], self.font.size(self.get_text())[1])

    def get_label(self):
        """
        :return: Text for this option 
        """
        return str(self.race)

    def draw(self, surface, position):
        """
        Draw on given surface.
        :param surface: Surface to draw
        :type surface: Surface
        :param position: Position to draw
        :type position: Point
        """
        label = self.font.render(self.get_text(), 1, self.race.get_color())
        font_point = self.get_size().scale(0.5)
        top_left_corner = position - font_point
        surface.blit(label, top_left_corner.to_tuple())


class MapToLoadOption(SettingOption):
    """
    Option for race setting.
    """

    def __init__(self, driver, parent, map_data):
        """
        Constructor.
        :param driver: Current game driver
        :type driver: Driver
        :param parent: Underlying menu item.
        :type parent: Setting
        :param map_data: map for this option.
        """
        super(MapToLoadOption, self).__init__(driver, parent)
        self.map_data = map_data

    def select(self):
        """
        Select option. Change settings accordingly.
        """
        self.driver.map_to_load = self.map_data

    def get_size(self):
        """
        :return: Size
        :rtype: Point
        """
        return Point(self.font.size(self.get_text())[0], self.font.size(self.get_text())[1])

    def get_label(self):
        """
        :return: Text for this option 
        """
        return str(self.map_data[NAME_FIELD])

    def draw(self, surface, position):
        """
        Draw on given surface.
        :param surface: Surface to draw
        :type surface: Surface
        :param position: Position to draw
        :type position: Point
        """
        label = self.font.render(self.get_text(), 1, THECOLORS['black'])
        font_point = self.get_size().scale(0.5)
        top_left_corner = position - font_point
        surface.blit(label, top_left_corner.to_tuple())


class AmountOption(SettingOption):
    """
    Option for general amount settings.
    """

    # TODO: Improve implementation, use a single object. Shouldn't be hard.

    def __init__(self, driver, parent, amount):
        """
        Constructor.
        :param driver: Current game driver
        :type driver: Driver
        :param parent: Underlying menu item.
        :type parent: Setting
        :param amount: Amount for this option.
        """
        super(AmountOption, self).__init__(driver, parent)
        self.amount = amount

    @abc.abstractmethod
    def select(self):
        """
        Select option. Change settings accordingly.
        """
        pass

    def get_size(self):
        """
        :return: Size
        :rtype: Point
        """
        return Point(self.font.size(self.get_text())[0], self.font.size(self.get_text())[1])

    def get_label(self):
        """
        :return: Text for this option 
        """
        return str(self.amount)

    def draw(self, surface, position):
        """
        Draw on given surface.
        :param surface: Surface to draw
        :type surface: Surface
        :param position: Position to draw
        :type position: Point
        """
        label = self.font.render(self.get_text(), 1, THECOLORS['black'])
        font_point = self.get_size().scale(0.5)
        top_left_corner = position - font_point
        surface.blit(label, top_left_corner.to_tuple())


class EnemyAmount(AmountOption):
    """
    Sets amount of enemies for random match.
    """

    def select(self):
        """
        Handle. 
        """
        self.driver.amount_of_enemies = self.amount

    def get_label(self):
        """
        :return: Text for this option 
        """
        return str(self.amount)


class ColonyAmount(AmountOption):
    """
    Sets amount of empty colonies for random match.
    """

    def select(self):
        """
        Handle. 
        """
        self.driver.amount_of_empty_colonies = self.amount

    def get_label(self):
        """
        :return: Text for this option 
        """
        return str(self.amount)
