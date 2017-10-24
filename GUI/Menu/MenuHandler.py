"""
Menu handlers.
"""

import abc


class MenuHandler:
    """
    A menu handler. Implements common functionality.
    """
    def __init__(self, driver):
        """
        Constructor.
        :param driver: Driver
        """
        self.driver = driver

    @abc.abstractmethod
    def handle(self):
        """
        Handle.
        """
        pass


class StartGameHandler(MenuHandler):
    """
    Triggers game start.
    """
    def handle(self):
        """
        Handle. 
        """
        self.driver.start_game()


class StartCustomMapHandler(MenuHandler):
    """
    Triggers game start.
    """
    def handle(self):
        """
        Handle. 
        """
        self.driver.start_custom_map_game()


class NextMenuHandler(MenuHandler):
    """
    Changes to another menu.
    """
    def __init__(self, driver, next_menu):
        super(NextMenuHandler, self).__init__(driver)
        self.next_menu = next_menu

    def handle(self):
        """
        Handle.
        """
        self.driver.set_menu(self.next_menu(self.driver))
        self.driver.move_alpha_to(self.driver.text_screen, 0, 255)


class QuitGameHandler(MenuHandler):
    """
    Quits game.
    """
    def handle(self):
        """
        Handle.
        """
        self.driver.quit()


class ChooseRaceHandler(MenuHandler):
    """
    Chose a race. Currently not in use due to a different visualization. May be useful.
    """
    def __init__(self, driver, race):
        super(ChooseRaceHandler, self).__init__(driver)
        self.race = race

    def handle(self):
        """
        Handle. 
        """
        self.driver.player_one.set_race(self.race)


class NullHandler(MenuHandler):
    """
    Does nothing. Null Object.
    """
    def __init__(self):
        super(NullHandler, self).__init__(None)

    def handle(self):
        """
        Handle.
        """
        pass


class UnPauseHandler(MenuHandler):
    """
    Unpause
    """
    def handle(self):
        """
        Handle. 
        """
        self.driver.pause_key()
