"""
Graphic party.
"""

import Settings.GUISettings
from GUI.GraphicObject import MovingObject
from GUI.Functions import draw_ngon
from GUI.Point import Point
from Party import Party
from Race import NullRace


class GraphicParty(MovingObject):
    """
    Graphic abstraction of a Party.
    """
    def __init__(self, a_map, party, position_i, radius, destination):
        """
        Constructor.
        :param a_map: Map which this object belongs to
        :type a_map: Map
        :param party: Logic colony
        :type party: Party
        :param position_i: Initial position
        :type position_i: Point
        :param destination: Destination
        """
        self.party = party
        super(GraphicParty, self).__init__(
            a_map, position_i, radius, destination, self.party.get_max_speed() * Settings.GUISettings.PARTY_SPEED_FACTOR
        )
        self.theta = 0
        self.hitbox = int(self.radius / 2)
        self.parameter = 0

    def tick(self):
        """
        Update object
        """
        super(GraphicParty, self).tick()
        self.theta += Settings.GUISettings.COLONY_SPIN_SPEED
        self.parameter += 1

    def draw(self, surface):
        """
        Draw on given surface.
        :param surface: Surface to draw on
        :type surface: Surface
        """
        self.party.draw(surface, self.radius, self.position, self.theta, self.parameter, self.speed)

    def collide(self, o):
        """
        Collide with another object.
        """
        if o == self.destination:
            self.arrived()
        else:
            self.avoid(o)

    def arrived(self):
        """
        Remove from its map.
        """
        self.destination.colony.accept(self.party)
        self.map.remove(self)

    def add_to_map(self):
        """
        Add to its map.
        """
        self.map.insert_graphic_party(self)

    # def avoid(self, gr_col):
    #     if gr_col.position.distance(self.position) > gr_col.radius * 1.4:
    #         return
    #     if not gr_col == self.destination and not gr_col.position.distance(self.position) == 0:
    #         self.external_acceleration += (self.position - gr_col.position).scale(
    #             gr_col.position.distance(self.position) ** Settings.GUIConfig.COLONY_PARTY_REPEL_FORCE_EXP)\
    #             .scale(Settings.GUIConfig.COLONY_PARTY_REPEL_FORCE)

    def avoid(self, gr_col):
        """
        Avoid another object.
        """
        self.external += self.position - gr_col.position

    def reset_ext_forces(self):
        """
        Reset external forces.
        """
        self.external = Point(0, 0)


class BackgroundParty(GraphicParty):
    """
    Graphic party for Background.
    """
    def __init__(self, a_map, position_i, position_f, radius, max_speed):
        super(BackgroundParty, self).__init__(a_map, Party(NullRace(), 0), position_i, radius, position_f)
        self.max_speed = max_speed

    def add_to_map(self):
        """
        Add to its map.
        """
        self.map.insert_background(self)

    def tick(self):
        """
        Update object
        """
        super(GraphicParty, self).tick()
        self.theta += Settings.GUISettings.BACKGROUND_SPIN_SPEED

    def arrived(self):
        """
        Remove from its map.
        """
        self.map.remove(self)

    def draw(self, surface):
        """
        Draw on given surface.
        :param surface: Surface to draw on
        :type surface: Surface
        """
        if not (-self.radius < self.position.x < self.map.width + self.radius
                and -self.radius < self.position.y < self.map.height + self.radius):
            self.remove()
        else:
            draw_ngon(surface, Settings.GUISettings.BACKGROUND_COLOR, 3, self.radius, self.position, self.theta)

    def move(self):
        """
        Update position.
        """
        self.acceleration = (self.destination - self.position).limit_size(1).scale(
            Settings.GUISettings.PARTY_ACCELERATION_FACTOR)
        self.speed = self.speed + self.acceleration
        self.speed.limit_size(self.max_speed)
        self.position = self.position + self.speed
