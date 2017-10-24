"""
Game driver and its stats. 
"""

from Settings import GUISettings
from Settings import MenuSettings
from GUI.Map import Map
from GUI.Point import Point
from MapLoader import MapLoader
from Player import *
from Race import NullRace
from SoundDriver import SoundDriver
from EventHandler import EventHandler
from RaceManager import RaceManager
from MapManager import *


class Driver:
    """
    Game driver. Sets matches, takes input, controls game flow and checks for a winner.
    """

    def __init__(self, map_screen, background_screen, text_screen):
        """
        Constructor.
        :param map_screen: Surface 
        :param background_screen: Surface
        :param text_screen: Surface
        """
        self.amount_of_enemies = 0
        self.amount_of_empty_colonies = 0
        self.map_to_load = None
        self.race_manager = RaceManager()
        self.human_players = []
        self.players = []
        self.map = Map(GUISettings.SCREEN_WIDTH, GUISettings.SCREEN_HEIGHT)
        self.event_handler = EventHandler(self)
        self.screen = map_screen
        self.background_screen = background_screen
        self.player_one = Player()
        self.human_players.append(self.player_one)
        self.sound_driver = SoundDriver()
        self.map_loader = MapLoader(self)
        self.text_screen = text_screen
        self.running = True
        self.map_manager = MapManager()
        self.state = MainMenu(self)
        self.menu = MenuSettings.MAIN_MENU(self)

    def get_races(self):
        """
        :return: Dictionary with available races 
        """
        return self.race_manager.get_races()

    def get_races_array(self):
        """
        :return: Array with available races 
        """
        return self.race_manager.get_races_array()

    def get_maps(self):
        """
        :return: Dictionary with available maps 
        """
        return self.map_manager.get_maps()

    def get_maps_array(self):
        """
        :return: Array with available maps 
        """
        return self.map_manager.get_maps_array()

    def is_running(self):
        """
        :return: True if the game is running and False otherwise
        :rtype: bool
        """
        return self.running

    def quit(self):
        """
        Set running state to False. 
        """
        self.running = False

    def load_map(self):
        """
        Load map from selected data.
        """
        # Clear players
        self.players = []
        # Load map
        self.map_loader.load_in_map(self.map_to_load, self.map, self.human_players)
        # Set new players
        self.players = self.map_loader.players

    def add_random_player(self):
        """
        Add an enemy with a random race.
        """
        self.players.append(RandomPlayer())

    def set_player_name(self, name):
        """
        Set a name for the player.
        :param name: Name to set
        """
        # TODO: Set and use player name
        self.player_one.set_name(name)

    def set_player_race(self, race):
        """
        Set race for the human player.
        :param race: Race to set
        """
        self.player_one.set_race(race)

    def get_player_name(self):
        """
        :return: Player's name 
        """
        return self.player_one.name

    def get_player_race(self):
        """
        :return: Player's race 
        """
        return self.player_one.race

    def add_player(self, player):
        """
        :param player: Add a new player to the game 
        """
        self.players.append(player)

    def check_winning_condition(self):
        """
        Check if there's a winner. A race is the winning race when there are no other races on the map.
        :return The winner
        :rtype AbstractRace
        """
        win = NullRace()
        for gr_col in self.map.graphic_colonies:
            race = gr_col.colony.race
            if win.same_type(NullRace()):
                win = race
            if not race.same_type(NullRace()) and not race.same_type(win):
                return NullRace()
        for gr_pty in self.map.graphic_parties:
            if not gr_pty.party.race.same_type(win):
                return NullRace()
        self.won(win)
        return win

    def won(self, race):
        """
        React after a winner has been found.
        :param race: Winning race
        :type race: AbstractRace
        """
        self.state.won(race)

    def set_state(self, state):
        """
        Change current game state.
        :param state: The new state
        :type state: GameState
        """
        self.state = state

    def tick(self):
        """
        Actions to perform every tick.
        """
        # Handle input
        self.handle_events()
        # Update background
        self.map.tick_background()
        # Draw background
        self.map.draw_background(self.background_screen)
        # Run main
        self.run()
        # Check for a winner
        self.check_winning_condition()

    def handle_events(self):
        """
        Ask the event handler to handle input. 
        """
        self.event_handler.handle_events()

    def run(self):
        """
        Run main, specified by current state.
        """
        self.state.run()

    def get_colonies_in(self, position):
        """
        Get colonies that contain given point.
        :param position: Point to scan
        :type position: Point
        :return: Array of colonies
        :rtype List
        """
        return self.map.get_colonies_in(position)

    def select(self, position):
        """
        Select given position and act according to current state.
        :param position: Position selected
        :type position: tuple
        """
        position = Point(position[0], position[1])
        self.state.select(position)

    def release_mouse(self, position):
        """
        Release mouse at given position and act according to current state.
        :param position: Position where release occurs
        :type position: tuple
        """
        position = Point(position[0], position[1])
        self.state.release_mouse(position)

    def hover(self, position):
        """
        Hover at given position and act according to current state.
        :param position: Position to hover
        :type position: tuple
        """
        position = Point(position[0], position[1])
        self.state.hover(position)

    def update_mouse_position(self, position):
        """
        Acknowledge current mouse position.
        :param position: Mouse position
        :type position: tuple
        """
        position = Point(position[0], position[1])
        self.state.update_mouse_position(position)

    def pause_key(self):
        """
        Pause key has been pressed.
        """
        self.state.pause()

    def main_menu_key(self):
        """
        Main menu key has been pressed.
        """
        self.state.main_menu_key()

    def selection_left(self):
        """
        Selection left key has been pressed.
        """
        self.state.selection_left()

    def selection_right(self):
        """
        Selection right key has been pressed.
        """
        self.state.selection_right()

    def selection_up(self):
        """
        Selection up key has been pressed.
        """
        self.state.selection_up()

    def selection_down(self):
        """
        Selection down key has been pressed.
        """
        self.state.selection_down()

    def select_key(self):
        """
        Selection key has been pressed.
        """
        self.state.select_key()

    def load_random_map(self):
        """
        Load a random map.
        """
        # Make screen transparent in one tick
        self.move_alpha_to(self.screen, 0, 255)
        # Remove all players
        self.players = []
        # Load map
        # # self.map_loader.load_in_map(FOUR_BASES, self.map, self.human_players)
        self.map_loader.load_random(self.map, self.amount_of_empty_colonies, 40, 60, self.human_players,
                                    self.amount_of_enemies, self.race_manager.get_races_array())
        # Retrieve players for this match
        self.players = self.map_loader.players

    @staticmethod
    def move_alpha_to(surface, target, speed=GUISettings.DEFAULT_ALPHA_CHANGE_SPEED):
        """
        Move alpha of a given surface towards a target value. 
        :param surface: Surface which alpha to change
        :type surface: Surface
        :param target: Target alpha value
        :type  target: int
        :param speed: Maximum change
        :type speed: int
        """
        current_alpha = surface.get_alpha()
        if not current_alpha == target:
            move_dir = (target - current_alpha) / abs(target - current_alpha)
            move_amount = min(speed, abs(target - current_alpha))
            surface.set_alpha(current_alpha + move_dir * move_amount)

    def start_game(self):
        """
        Start game. Load a map and change state.
        """
        self.load_random_map()
        self.set_state(InGame(self))

    def start_custom_map_game(self):
        """
        Start game. Load a map and change state.
        """
        self.load_map()
        self.set_state(InGame(self))

    def set_menu(self, menu):
        """
        Set current menu.
        :param menu: Next menu
        :type menu: Menu
        """
        self.menu = menu

    def play_select(self):
        """
        Play select sound.
        """
        self.sound_driver.play_select()

    def play_move_selection(self):
        """
        Play move selection sound.
        """
        self.sound_driver.play_move_selection()

    def play_taken(self):
        """
        Play taken sound.
        """
        self.sound_driver.play_taken()


class GameState:
    """
    Represents current game state. Is asked what to do on state dependent actions.
    """

    def __init__(self, driver):
        """
        Constructor.
        :param driver: Driver to control
        :type driver: Driver
        """
        self.driver = driver

    def run(self):
        """
        Run main. 
        """
        pass

    def set_state(self, state):
        """
        Set state of its driver.
        :param state: New state
        :type state: GameState
        """
        self.driver.set_state(state)

    def state_is_mainmenu(self):
        """
        :return: True if currently on main menu, False otherwise 
        """
        return False

    def state_is_paused(self):
        """
        :return: True if currently on pause, False otherwise 
        """
        return False

    def state_is_ingame(self):
        """
        :return: True if currently in game, False otherwise 
        """
        return False

    def state_is_finished(self):
        """
        :return: True if currently on a finished match, False otherwise 
        """
        return False

    def pause(self):
        """
        Pause.
        """
        pass

    def get_colonies_in(self, position):
        """
        Get colonies that contain given point.
        :param position: Point to scan
        :type position: Point
        """
        pass

    def select(self, position):
        """
        Select given position and act according to current state.
        :param position: Position selected
        :type position: Point
        """
        pass

    def release_mouse(self, position):
        """
        Release mouse at given position and act according to current state.
        :param position: Position where released occurs
        :type position: Point
        """
        pass

    def hover(self, position):
        """
        Hover at given position and act according to current state.
        :param position: Position to hover
        :type position: Point
        """
        pass

    def update_mouse_position(self, position):
        """
        Acknowledge current mouse position.
        :param position: Mouse position
        :type position: Point
        """
        pass

    def won(self, race):
        """
        Handle winning event.
        :param race: Winning race
        :type race: AbstractRace
        """
        pass

    def main_menu_key(self):
        """
        Main menu key has been pressed.
        """
        self.set_state(MainMenu(self.driver))

    def selection_left(self):
        """
        Selection left key has been pressed.
        """
        pass

    def selection_right(self):
        """
        Selection right key has been pressed.
        """
        pass

    def selection_up(self):
        """
        Selection up key has been pressed.
        """
        pass

    def selection_down(self):
        """
        Selection down key has been pressed.
        """
        pass

    def select_key(self):
        """
        Selection key has been pressed.
        """
        pass


class OnMenuState(GameState):
    """
    State for common functionality among menus.
    """

    def __init__(self, driver):
        super(OnMenuState, self).__init__(driver)
        self.driver.text_screen.set_alpha(0)

    def run(self):
        """
        Run main. Doesn't tick map.
        """
        # Move alpha to full opaqueness
        self.driver.move_alpha_to(self.driver.text_screen, 255, 5)
        # Tick Menu
        self.driver.menu.tick()
        # Draw menu
        self.driver.menu.draw(self.driver.text_screen)

    def release_mouse(self, position):
        """
        Handle mouse release.
        :param position: Position where release occurs
        :type position: Point
        """
        self.driver.menu.release_mouse(position)

    def hover(self, position):
        """
        Handle hover.
        :param position: Position to hover
        :type position: Point
        """
        self.driver.menu.hover(position)

    def selection_left(self):
        """
        Move selection.
        """
        self.driver.menu.selection_left()

    def selection_right(self):
        """
        Move selection.
        """
        self.driver.menu.selection_right()

    def selection_up(self):
        """
        Move selection.
        """
        self.driver.menu.selection_up()

    def selection_down(self):
        """
        Move selection.
        """
        self.driver.menu.selection_down()

    def update_mouse_position(self, position):
        """
        Update current mouse position.
        :param position: Current position
        :type position: Point
        """
        self.driver.menu.update_mouse_position(position)

    def select_key(self):
        """
        Select. 
        """
        self.driver.menu.select_key()


class MainMenu(OnMenuState):
    """
    On main menu.
    """

    def __init__(self, driver):
        super(MainMenu, self).__init__(driver)
        self.driver.menu = MenuSettings.MAIN_MENU(self.driver)

    def state_is_mainmenu(self):
        """
        :return: True 
        """
        return True

    def run(self):
        """
        Run parent
        """
        super(MainMenu, self).run()


class Paused(OnMenuState):
    """
    On pause.
    """

    def __init__(self, driver):
        super(Paused, self).__init__(driver)
        self.driver.menu = MenuSettings.PAUSE_MENU(self.driver)
        self.driver.play_select()

    def state_is_paused(self):
        """
        :return: True 
        """
        return True

    def pause(self):
        """
        Unpause actually.
        """
        self.set_state(InGame(self.driver))
        self.driver.play_select()

    def run(self):
        """
        Draw static map, make semi-transparent and run parent.
        """
        self.driver.map.draw(self.driver.screen)
        self.driver.move_alpha_to(self.driver.screen, GUISettings.PAUSE_ALPHA)
        super(Paused, self).run()


class MatchFinished(OnMenuState):
    """
    Match is finished.
    """

    def __init__(self, driver, winning_race):
        super(MatchFinished, self).__init__(driver)
        self.driver.menu = MenuSettings.MATCH_FINISHED_MENU(self.driver, winning_race)

    def run(self):
        """
        Tick map and draw map, clear selection, make map transparent slowly.
        """
        self.driver.map.is_over = True
        self.driver.map.tick()
        self.driver.map.clear_selection()
        self.driver.map.draw(self.driver.screen)
        self.driver.move_alpha_to(self.driver.screen, 0, GUISettings.FINISHED_ALPHA_CHANGE_SPEED)
        super(MatchFinished, self).run()

    def state_is_finished(self):
        """
        :return: True 
        """
        return True


class InGame(GameState):
    """
    In game.
    """

    def __init__(self, driver):
        super(InGame, self).__init__(driver)
        self.driver.map.is_over = False

    def state_is_ingame(self):
        """
        :return: True 
        """
        return True

    def won(self, race):
        """
        There's a winner. Change state to finished.
        :param race: Winner
        :type race: AbstractRace
        """
        self.set_state(MatchFinished(self.driver, race))

    def run(self):
        """
        Remove text screen, tick map and players, and draw the map.
        :return: 
        """
        self.driver.move_alpha_to(self.driver.text_screen, 0)
        for p in self.driver.players:
            p.tick(self.driver.map)
        self.driver.map.tick()
        self.driver.map.draw(self.driver.screen)
        self.driver.menu.draw(self.driver.text_screen)
        self.driver.move_alpha_to(self.driver.screen, 255)

    def pause(self):
        """
        Pause. 
        """
        self.set_state(Paused(self.driver))

    def get_colonies_in(self, position):
        """
        :param position: Position to scan
        :type position: Point
        :return: Colonies that contain given point
        """
        return self.driver.get_colonies_in(position)

    def select(self, position):
        """
        Select colonies.
        :param position: Position to select
        :type position: Point
        """
        colonies = self.get_colonies_in(position)
        for c in colonies:
            self.driver.map.select(c, self.driver.get_player_race())

    def release_mouse(self, position):
        """
        Send parties from selection to colony in position.
        :param position: Position at release
        :type position: Point
        """
        colonies = self.get_colonies_in(position)
        for c in colonies:
            self.driver.map.send_to(c, self.driver.get_player_race())
        self.driver.map.clear_selection()

    def update_mouse_position(self, position):
        """
        Update mouse position. Map handles hovers on its own.
        :param position: Current position.
        :type position: Point
        """
        self.driver.map.update_mouse_position(position)
