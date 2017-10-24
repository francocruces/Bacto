"""
Party. Represents a moving group of units. 
"""


class Party:
    """
    A party of moving units. Merely logic.
    """
    def __init__(self, race, size, str_factor=1, spd_factor=1):
        """
        Constructor.
        :param race:
        :type race: AbstractRace
        :param size: 
        :type size: int
        :param str_factor: Strength factor given by colony
        :param spd_factor: Strength factor given by colony
        """
        self.race = race
        self.size = size
        self.str_factor = str_factor
        self.spd_factor = spd_factor

    def enter_colony(self, colony):
        """
        Enter given colony.
        :param colony: Colony in which to enter
        :type colony: AbstractColony
        """
        colony.accept(self)

    def get_max_speed(self):
        """
        Get max party speed.
        :return: Max speed
        :rtype float
        """
        return self.race.speed * self.spd_factor

    def get_color(self):
        """
        Get color of this party.
        :return: Party color
        :rtype tuple
        """
        return self.race.get_color()

    def draw(self, surface, radius, position, theta, parameter, direction):
        """
        Make race to draw a party.
        :param surface: Surface to draw
        :type surface: Surface
        :param radius: Party radius
        :param position: Party position
        :type position: Point
        :param theta: Angle
        :param parameter: Animation parameter
        :param direction: Current moving direction
        :type direction: Point
        """
        self.race.draw_party(surface, radius, position, theta, parameter, direction)
