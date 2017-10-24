"""
Point.
"""

import numpy as np


class Point(object):
    """
    A point in the two dimensional space.
    """

    def __init__(self, x, y):
        """
        Constructor.
        
        :param x: Horizontal position
        :type x: float
        :param y: Vertical position
        :type y: float
        """
        self.x = x
        self.y = y

    def normal(self, p):
        """
        Get normal vector for segment between two points. Currently on simplified version.
        :param p: Another point
        :type p: Point
        :return: Point representing normal direction
        :rtype: Point
        """
        d = p - self
        return Point(-d.y, d.x)

    def distance(self, p):
        """
        Get distance between two points.
        :param p: Another point
        :type p: Point
        """
        return pow(pow(self.x - p.x, 2) + pow(self.y - p.y, 2), 1 / 2)

    def mid_point(self, p):
        """
        Return a new point in the middle of two.
        :param p: Another point
        :type p: Point
        :return: Midpoint
        :rtype: Point
        """
        return Point((p.x + self.x) / 2, (p.y + self.y) / 2)

    def move(self, direction, amount):
        """
        Move point in given direction a given amount.
        :param direction: 
        :type direction: Point
        :param amount: 
        :type amount: int
        """
        self.x += direction.x * amount
        self.y += direction.y * amount

    def copy(self):
        """
        Copy given point.
        :return: A copy
        :rtype: Point
        """
        return Point(self.x, self.y)

    def discretize(self):
        """
        Discretize coordinates.
        """
        self.x = int(self.x)
        self.y = int(self.y)
        return self

    def slope(self, p):
        """
        Compute slope of segment between two points. Return NaN if infinite.
        :param p: Another point
        :type p: Point
        :return: Slope from self to p
        :rtype: float
        """
        if (self.x - p.x) == 0:
            return np.nan
        else:
            return (self.y - p.y) / (self.x - p.x)

    def get_discrete_segment(self, p):
        """
        Create a discrete segment between two points.
        :param p: Another point
        :type p: Point
        :return: List of Points conforming the segment between both points
        """
        result = []
        a = self.copy().discretize()
        b = p.copy().discretize()
        slope = a.slope(b)

        increment = 1
        if a.x > b.x:
            increment = -1

        for x in range(int(a.x), int(b.x), increment):
            if ~np.isnan(slope):
                y = ((x - a.x) * slope) + a.y
            else:
                y = a.y
            result.append(Point(int(x), int(y)))
        return result

    def __add__(self, other):
        """
        Adds points.
        :param other: Another point
        :type other: Point
        :return: Result
        """
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """
        Subs points.
        :param other: Another point
        :type other: Point
        :return: Result
        """
        return Point(self.x - other.x, self.y - other.y)

    def scale(self, factor):
        """
        Scale point to origin in given factor.
        :param factor: 
        """
        self.x *= factor
        self.y *= factor
        return self

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def size(self):
        """
        :return: Distance from (0, 0) 
        """
        return self.distance(Point(0, 0))

    def limit_size(self, size):
        """
        Reduce size to given value.
        """
        if self.size() > size:
            self.scale(size / self.size())
        return self

    def to_tuple(self):
        """
        :return: Point as a tuple 
        """
        return self.x, self.y

    def normalize(self, size):
        """
        Change size to given value.
        :return: Self, for chaining 
        """
        self.scale(size / self.size())
        return self
