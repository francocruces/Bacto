import numpy as np

from Colony import RegularColony
from Settings.ColonySettings import *
from Settings.GUISettings import *
from GUI.GraphicColony import GraphicColony
from GUI.Point import Point
from Player import RandomPlayer
from Race import NullRace
from MapManager import *

class MapLoader:
    def __init__(self, driver):
        self.players = []
        self.driver = driver

    def load_in_map(self, map_data, a_map, human_players):
        print("LOADING MAP")
        a_map.empty()
        players = human_players.copy()
        enemies = []
        scale_ratio = a_map.width / 1600
        for i in range(map_data[N_ENEMIES_FIELD]):
            new = RandomPlayer()
            print("ADDING " + str(new.name))
            new.random_race(players, self.driver.get_races_array())
            players.append(new)
            enemies.append(new)
        for i in map_data[PLAYER_COL_FIELD]:
            print("ADDING PLAYER COLONY")
            colony = i[0]
            colony.empty()
            colony.set_size(INITIAL_PLAYER_COLONY_SIZE)
            colony.set_race(players[i[1]].race)
            GraphicColony(a_map, colony, i[2].copy().scale(scale_ratio), i[3] * scale_ratio)
        for i in map_data[ENEMY_COL_FIELD]:
            print("ADDING ENEMY COLONY")
            colony = i[0]
            colony.empty()
            colony.set_size(INITIAL_PLAYER_COLONY_SIZE)
            colony.set_race(enemies[i[1]].race)
            GraphicColony(a_map, colony, i[2].copy().scale(scale_ratio), i[3] * scale_ratio)
        for i in map_data[EMPTY_COL_FIELD]:
            print("ADDING EMPTY COLONY")
            colony = i[0]
            colony.empty()
            colony.set_size(INITIAL_NULL_COLONY_SIZE)
            colony.set_race(NullRace())
            GraphicColony(a_map, colony, i[2].copy().scale(scale_ratio), i[3] * scale_ratio)

        self.players = players
        print("LOADED")

    def load_random(self, a_map, n_colonies, min_size, max_size, human_players, n_enemies, possible_races):
        a_map.empty()
        n_players = len(human_players) + n_enemies
        theta = np.random.rand(1)[0] * 2 * np.pi
        center = Point(a_map.width / 2, a_map.height / 2)
        for human in human_players:
            position = Point(
                np.cos(theta) * (a_map.width / 2 - INITIAL_COLONIES_RADIUS),
                np.sin(theta) * (a_map.height / 2 - INITIAL_COLONIES_RADIUS),
            ) + center
            GraphicColony(a_map, RegularColony(human.race, INITIAL_PLAYER_COLONY_SIZE), position, INITIAL_COLONIES_RADIUS)
            theta += (2 * np.pi) / n_players
        other_players = human_players.copy()
        for i in range(n_enemies):
            position = Point(
                np.cos(theta) * (a_map.width / 2 - INITIAL_COLONIES_RADIUS),
                np.sin(theta) * (a_map.height / 2 - INITIAL_COLONIES_RADIUS),
            ) + center
            enemy = RandomPlayer(other_players)
            enemy.random_race(other_players, possible_races)
            other_players.append(enemy)
            GraphicColony(a_map, RegularColony(enemy.race, INITIAL_PLAYER_COLONY_SIZE), position, INITIAL_COLONIES_RADIUS)

            theta += (2 * np.pi) / n_players
        self.players = other_players
        for i in range(n_colonies):
            while True:
                radius = np.random.randint(min_size, max_size)
                position = Point(
                    np.random.randint(radius, a_map.width - radius),
                    np.random.randint(radius, a_map.height - radius)
                )
                if a_map.can_place_colony(radius, position):
                    GraphicColony(a_map, RegularColony(NullRace(), INITIAL_NULL_COLONY_SIZE), position, radius)
                    break
                else:
                    print("Can't place random colony. Generating a new one.")
        pass
