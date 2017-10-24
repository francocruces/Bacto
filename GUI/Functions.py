import pygame
import numpy as np
from Settings.GUISettings import *
from GUI.Point import Point


def draw_ngon(surface, color, n, radius, position, theta=0.0):
    """
    Draws a polygon with n sides
    :param surface: Surface to draw
    :param color: Polygon color
    :param n: Number of sides
    :param radius: Polygon radius
    :param position: Position
    :param theta: Rotation angle 
    :return: 
    """
    pi2 = 2 * np.pi
    position.discretize()
    for i in range(0, n):
        pygame.draw.line(surface, color, (position.x, position.y),
                         (np.cos(i / n * pi2 + theta) * radius + position.x,
                          np.sin(i / n * pi2 + theta) * radius + position.y), POLYGON_INNER_WIDTH)

    return pygame.draw.lines(surface,
                             color,
                             True,
                             [(np.cos(i / n * pi2 + theta) * radius + position.x,
                               np.sin(i / n * pi2 + theta) * radius + position.y)
                              for i in range(0, n)], POLYGON_OUTER_WIDTH)


def draw_spin(surface, radius, position, theta, parameter, direction, color, sides):
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
    theta = theta * BALANCED_SPIN_SPEED
    draw_ngon(surface, color, sides, radius, position, theta)


def draw_drone(surface, radius, position, theta, parameter, direction, color, sides):
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
    if direction.x == 0:
        angle = np.pi / 2
    else:
        angle = np.arctan(direction.y / direction.x)
    if direction.x > 0:
        angle += np.pi / 6
    else:
        angle -= np.pi / 6
    theta_1 = angle
    theta_2 = angle + np.pi * 2 / 6
    position_1 = position + Point(-direction.y, direction.x).limit_size(1).scale(radius / 2)
    position_2 = position + Point(direction.y, -direction.x).limit_size(1).scale(radius / 2)
    draw_ngon(surface, color, sides, radius / 2, position_1, theta_1)
    draw_ngon(surface, color, sides, radius / 2, position_2, theta_2)


def draw_eccentric(surface, radius, position, theta, parameter, direction, color, sides):
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
    theta = theta * FERTILE_SPIN_SPEED
    new_position = position + Point(
        np.cos(parameter * FERTILE_ANIMATION_SPEED) * radius * FERTILE_ANIMATION_AMP,
        np.sin(parameter * FERTILE_ANIMATION_SPEED) * radius * FERTILE_ANIMATION_AMP
    )
    draw_ngon(surface, color, sides, radius * 2 / 3, new_position, theta)


def draw_change_radius(surface, radius, position, theta, parameter, direction, color, sides):
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
    :param color: Color
    :type color: tuple
    :param sides: Number of sides of drawn polygon
    """
    radius = radius + np.sin(parameter * TANK_ANIMATION_SPEED / (2 * np.pi)) * TANK_ANIMATION_AMP
    draw_ngon(surface, color, sides, radius, position, theta)

DRAW_FUNCTIONS = {
    "spin": draw_spin,
    "eccentric": draw_eccentric,
    "change_radius": draw_change_radius,
    "drone": draw_drone
}
