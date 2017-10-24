"""
Colony.
"""

import math
from Settings.ColonySettings import *
from Party import Party
from Race import NullRace


class AbstractColony:
    """
    A colony. Merely logic.
    """

    def __init__(self, race=NullRace(), size=0, def_factor=1, str_factor=1, repr_factor=1, spd_factor=1):
        """
        Construct.
        :param race: Initial race
        :type race: AbstractRace
        :param size: Initial size
        :param def_factor: Defense modifier for battles
        :type def_factor: float
        :param str_factor: Strength modifier for battles
        :type str_factor: float
        :param repr_factor: Reproduction time factor 
        :type repr_factor: float
        :param spd_factor: Speed factor for moving
        :type spd_factor: float
        """
        self.race = race
        self.size = size
        self.def_factor = def_factor
        self.str_factor = str_factor
        self.repr_factor = repr_factor
        self.spd_factor = spd_factor
        self.time = 0

    def tick(self):
        """
        Grow. 
        """
        self.grow()

    def set_size(self, size):
        """
        Set size
        """
        self.size = size

    def set_race(self, race):
        """
        Set race
        :param race: New race
        :type race: AbstractRace
        """
        self.race = race

    def get_race(self):
        """
        :return: Race 
        """
        return self.race

    def accept(self, party):
        """
        Accept a party.
        :param party: Arriving party
        :type party: Party
        """
        if party.race.same_type(self.race):
            self.add(party)
        else:
            self.battle(party)

    def add(self, party):
        """
        Add incoming party
        :param party: Arriving party 
        :type party: Party
        """
        self.size = min(self.size + party.size, POPULATION_LIMIT)

    def battle(self, party):
        """
        Battle incoming party
        :param party: Arriving party
        :type party: Party
        """
        # Get battle power for each side
        net_col_def = self.race.defense * self.def_factor
        net_pty_str = party.race.strength * party.str_factor
        col_bp = self.size * net_col_def
        pty_bp = party.size * net_pty_str

        # Compute difference
        dif = col_bp - pty_bp

        # Write result
        self.size = max(dif // net_col_def, 0)
        party.size = max(-dif // net_pty_str, 0)

        # Decide ownership
        self.choose_winner(party)

    def choose_winner(self, party):
        """
        Set new owner after fight
        :param party: Post fight party
        :type party: Party
        """
        if self.size < party.size:
            self.size = party.size
            self.race = party.race
        else:
            if self.size == party.size:
                self.race = NullRace()

    def create_party(self):
        """
        Create a party with half the units inside. 
        :return: New party
        """
        party = Party(self.race, int(math.ceil(self.size / 2)), self.str_factor, self.spd_factor)
        self.size = math.floor(self.size / 2)
        return party

    def grow(self):
        """
        Grow once.
        """
        if self.size < POPULATION_LIMIT:
            self.time += 1
            if (self.time // int(self.race.reproduction_time * self.repr_factor)) > 0:
                self.size += 1
                self.time = 0

    def get_color(self):
        """
        :return: Color of current owner 
        """
        return self.race.get_color()

    def empty(self):
        """
        Remove all units from itself.
        """
        self.size = 0


class StrengthColony(AbstractColony):
    """
    Colony that increases strength of outgoing parties.
    """
    def __init__(self, race=NullRace(), size=0):
        super(StrengthColony, self).__init__(race, size, str_factor=1.3)


class SpeedColony(AbstractColony):
    """
    Colony that increases speed of outgoing parties.
    """
    def __init__(self, race=NullRace(), size=0):
        super(SpeedColony, self).__init__(race, size, spd_factor=1.3)


class RegularColony(AbstractColony):
    """
    Regular colony, no modifiers.
    """
    def __init__(self, race=NullRace(), size=0):
        super(RegularColony, self).__init__(race, size)


class GrowthColony(AbstractColony):
    """
    Colony with decreased reproduction time.
    """
    def __init__(self, race=NullRace(), size=0):
        super(GrowthColony, self).__init__(race, size, repr_factor=0.7)


class DefenseColony(AbstractColony):
    """
    Colony with increased defense.
    """
    def __init__(self, race=NullRace(), size=0):
        super(DefenseColony, self).__init__(race, size, def_factor=1.3)
