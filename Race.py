"""
Races. Represent unit category, with their stats, color, name and animation function.
"""

from GUI.Functions import *
from Settings.RaceSettings import *
from Settings.GUISettings import *
from GUI.colordict import THECOLORS


class Race:
    """
    Common functionality for races.
    """

    def __init__(self, race_id, name, strength, defense, speed, reproduction_time, animation_id, color, n_sides):
        self.speed = int(speed)
        self.reproduction_time = int(reproduction_time)
        self.strength = int(strength)
        self.defense = int(defense)
        self.name = name
        self.id = race_id
        self.animation_id = animation_id
        self.n_sides = int(n_sides)
        self.color = color

    def same_type(self, other):
        """
        :type other: Race
        :return: True if both race are same type, False otherwise 
        """
        return self.id == other.id

    def set_speed(self, speed):
        """
        Set speed of this race.
        :param speed: New speed
        :type speed: float
        """
        self.speed = speed

    def set_reproduction_time(self, reproduction_time):
        """
        Set reproduction time of this race.
        :param reproduction_time: New speed
        :type reproduction_time: float
        """
        self.reproduction_time = reproduction_time

    def set_strength(self, strength):
        """
        Set strength of this race.
        :param strength: New speed
        :type strength: float
        """
        self.strength = strength

    def set_defense(self, defense):
        """
        Set defense of this race.
        :param defense: New speed
        :type defense: float
        """
        self.defense = defense

    def get_color(self):
        """
        :return This race's color
        """
        return THECOLORS[self.color]

    def draw_party(self, surface, radius, position, theta, parameter, direction):
        """
        Draw a party.
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
        DRAW_FUNCTIONS[self.animation_id](
            surface, radius, position, theta, parameter, direction, self.get_color(), self.n_sides
        )

    def __str__(self):
        return self.name


class NullRace(Race):
    """
    Null race.
    """
    def __init__(self):
        super(NullRace, self).__init__(
            NULL_ID,
            NULL_NAME,
            NULL_STRENGTH,
            NULL_DEFENSE,
            NULL_SPEED,
            NULL_REPRODUCTION_TIME,
            NULL_ANIMATION_ID,
            NULL_COLOR,
            NULL_SIDES
        )
