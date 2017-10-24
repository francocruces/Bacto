"""
Graphic colony.
"""

import pygame
from Settings import ColonySettings
from Settings import GUISettings
from GUI.GraphicObject import MovingObject
from GUI.Functions import draw_ngon
from GUI.GraphicParty import GraphicParty
from GUI.Point import Point


class GraphicColony(MovingObject):
    """
    Graphic abstraction of a Colony.
    """
    def __init__(self, a_map, colony, position, radius):
        """
        Constructor.
        :param a_map: Map which this object belongs to
        :type a_map: Map
        :param colony: Logic colony
        :type colony: AbstractColony
        :param position: Colony Position
        :param radius: Colony radius
        """
        super(GraphicColony, self).__init__(a_map, position, radius, position, GUISettings.COLONY_MAX_SPEED)
        self.colony = colony
        self.theta = 0
        self.hitbox = int(self.hitbox * 5 / 6)
        self.text = ""
        self.font = pygame.font.Font("res/Cabin-Bold.ttf", 25)
        self.font.set_bold(True)

    def arrived(self):
        """
        Handle arrival to destination. 
        """
        pass

    def avoid(self, o):
        """
        Avoid another object. Use with acceleration for a smooth visual effect.
        """
        # TODO: Implement. Avoid other colonies
        # TODO: Acceleration based on size
        pass

    def tick(self):
        """
        Update graphic colony.
        """
        if not self.map.is_over:
            self.colony.tick()
        self.text = str(self.colony.size)
        self.theta += self.get_rot_speed()

    def collide(self, o):
        """
        Collide with another object.
        """
        pass

    def draw(self, surface):
        """
        Draw on given surface.
        :param surface: Surface to draw on
        :type surface: Surface
        """
        draw_ngon(surface, self.colony.get_color(), 4, self.radius, self.position, self.theta)
        label = self.font.render(self.text, 1, GUISettings.COLONY_NUMBER_COLOR)
        font_point = Point(self.font.size(self.text)[0], self.font.size(self.text)[1]).scale(0.5)
        surface.blit(label, (self.position - font_point).to_tuple())

    def add_to_map(self):
        """
        Add to its map.
        """
        self.map.insert_graphic_colony(self)

    def get_rot_speed(self):
        """
        :return: Rotation speed. 
        """
        return (0.25 - 0.005) * self.colony.size / ColonySettings.POPULATION_LIMIT + 0.01

    def send_party(self, destination):
        """
        Send a party towards another colony.
        :param destination: Target colony
        :type destination: GraphicColony
        """
        return GraphicParty(self.map, self.colony.create_party(), self.position,
                            (GUISettings.MAX_PARTY_COLONY_RATIO * self.radius - GUISettings.MIN_PARTY_SIZE) *
                            self.colony.size / ColonySettings.POPULATION_LIMIT + GUISettings.MIN_PARTY_SIZE,
                            destination)

    def get_race(self):
        """
        :return Race currently controlling this colony
        """
        return self.colony.get_race()
