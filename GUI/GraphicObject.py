"""
Common functionality for graphic objects.
"""

import abc
import Settings.GUISettings
from GUI.Point import Point


class AbstractGraphicObject:
    """
    A graphic object in a map.
    """
    def __init__(self, a_map, position, radius):
        """
        Constructor.
        :param a_map: 
        :param position:
        :type position: Point
        :param radius: 
        """
        self.map = a_map
        self.position = position
        self.radius = radius
        self.hitbox = self.radius
        self.add_to_map()

    @abc.abstractmethod
    def collide(self, o):
        """
        Collide with given object.
        """
        pass

    @abc.abstractmethod
    def add_to_map(self):
        """
        Add itself to its map.
        """
        pass

    def remove(self):
        """
        Remove from its map.
        """
        self.map.remove(self)

    @abc.abstractmethod
    def draw(self, surface):
        """
        Draw on given surface.
        :type surface: Surface
        """
        pass

    @abc.abstractmethod
    def tick(self):
        """
        Update this object. 
        """
        pass

    def contains(self, position):
        """        
        :type position: Point  
        :return: True if given position is contained in this object, False otherwise.
        """
        return position.distance(self.position) < self.radius


class MovingObject(AbstractGraphicObject):
    """
    An object that moves towards a destination.
    """
    def __init__(self, a_map, position, radius, destination, max_speed):
        """
        Constructor
        :param a_map: Map which this object belongs to 
        :type a_map: Map
        :param position: Object's position
        :type position: Point
        :param destination: Object's moving destination
        :type destination: GraphicColony
        :param max_speed: Object's max speed
        """
        super(MovingObject, self).__init__(a_map, position, radius)
        self.destination = destination
        self.speed = Point(0, 0)
        self.acceleration = Point(0, 0)
        self.max_speed = max_speed
        self.external = Point(0, 0)

    def tick(self):
        """
        Update object's position.
        """
        self.move()

    def set_max_speed(self, new_max_speed):
        """
        Set max speed
        :param new_max_speed: New max speed
        :type new_max_speed: float 
        """
        self.max_speed = new_max_speed
        return self

    def move(self):
        """
        Update position
        """
        # Set speed towards destination
        self.speed = (self.destination.position - self.position).limit_size(self.max_speed)
        # Add external speed and adjust to avoid getting stuck
        self.speed += self.external.limit_size(self.max_speed).copy().scale(
            Settings.GUISettings.PARTY_EXTERNAL_SPEED_ADJUST
        )
        # Normalize speed
        self.speed.normalize(self.max_speed)

        # Effectively move
        self.position = self.position + self.speed

    @abc.abstractmethod
    def arrived(self):
        """
        Handle arrival to destination. 
        """
        pass

    @abc.abstractmethod
    def collide(self, o):
        """
        Collide with an object.
        :param o: Object to collide with
        """
        pass

    @abc.abstractmethod
    def add_to_map(self):
        """
        Add to its map.
        """
        pass

    @abc.abstractmethod
    def avoid(self, o):
        """
        Avoid given object.
        :param o: Object to avoid 
        """
        pass
