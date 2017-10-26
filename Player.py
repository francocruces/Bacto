"""
Players.
"""

from Settings import PlayerSettings
from Race import *


class Player:
    """
    A human player.
    """
    def __init__(self, name="Player 1", race=NullRace()):
        """
        
        :param name: 
        :param race:
        :type race: AbstractRace
        """
        self.name = name
        self.race = race
        self.time = 0

    def set_name(self, name):
        """
        Set name. 
        """
        self.name = name

    def set_race(self, race):
        """
        Set race. 
        """
        self.race = race

    def tick(self, a_map):
        """
        On tick, do nothing
        """
        pass

    def get_race(self):
        """
        :return: Race 
        """
        return self.race


class NullPlayer(Player):
    """
    An NPC.
    """
    def __init__(self):
        super(NullPlayer, self).__init__("NullPlayer", NullRace())


class RandomPlayer(Player):
    """
    An enemy. Sets and plays randomly
    """
    def __init__(self, name="Enemy"):
        super(RandomPlayer, self).__init__(name, NullRace())

    def random_race(self, player_array, possible_races):
        """
        Set race randomly, different from existent ones.
        :param player_array: Array with existent players.
        """
        possible_races = possible_races.copy()
        for player in player_array:
            for r in possible_races:
                if player.race.same_type(r):
                    possible_races.remove(r)
        if not len(possible_races) == 0:
            self.race = possible_races[np.random.randint(0, len(possible_races))]
            print("New enemy: " + str(self.race))
        else:
            raise IndexError

    def tick(self, a_map):
        """
        Attack.
        :param a_map: Current map
        :type a_map: Map
        """
        if self.race.same_type(NullRace()):
            return
        self.time += 1
        if (self.time // PlayerSettings.ATTACK_EVERY) > 0:
            for c in a_map.graphic_colonies:
                if c.colony.race.same_type(self.race):
                    random = np.random.rand(1)
                    if random > PlayerSettings.ATTACK_PROBABILITY:
                        enemy_colonies = self.get_enemy_colonies(a_map)
                        target = enemy_colonies[np.random.randint(0, len(enemy_colonies))]
                        c.send_party(target)
            self.time = 0

    def get_enemy_colonies(self, a_map):
        result = []
        for c in a_map.graphic_colonies:
            if not c.colony.race.same_type(self.race):
                result.append(c)
        return result
