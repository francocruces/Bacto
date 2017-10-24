"""
Graphic settings. Change here how things are shown and animated.
"""

from GUI.colordict import THECOLORS

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

POLYGON_INNER_WIDTH = 2
POLYGON_OUTER_WIDTH = 2

COLONY_SPIN_SPEED = 0.05
COLONY_SPIN_SPEED_LOW = 0.05
COLONY_SPIN_SPEED_MEDIUM = 0.1
COLONY_SPIN_SPEED_HIGH = 0.2
COLONY_SPIN_SPEED_FULL = 0.3

COLONY_NUMBER_COLOR = THECOLORS['black']

PARTY_ACCELERATION_FACTOR = 0.2
PARTY_SPEED_FACTOR = 0.6
COLONY_PARTY_REPEL_FORCE_EXP = -2.8
COLONY_PARTY_REPEL_FORCE = 20
PARTY_COLONY_REPEL_FORCE = 0.03  # TODO: Use?
COLONY_COLONY_REPEL_FORCE = 0  # TODO: Use?
PARTY_SPEED_DECREASE_FACTOR = 0
PARTY_EXTERNAL_SPEED_ADJUST = 0.8

NULL_RACE_COLOR = THECOLORS['black']
BALANCED_RACE_COLOR = THECOLORS['red4']
FAST_RACE_COLOR = THECOLORS['green4']
FERTILE_RACE_COLOR = THECOLORS['yellow4']
TANK_RACE_COLOR = THECOLORS['blue4']

COLONY_SIZE_MIN = 30
COLONY_SIZE_MAX = 100
MAX_PARTY_COLONY_RATIO = 1.7
MIN_PARTY_SIZE = 20

COLONY_MAX_SPEED = 1

MAX_BACKGROUND_ELEMENTS = 6
MAX_BACKGROUND_SIZE = 500
BACKGROUND_COLOR = THECOLORS['gray69']
MAX_BACKGROUND_SPEED = 7
BACKGROUND_SPIN_SPEED = 0.025

INITIAL_COLONIES_RADIUS = 100

PAUSE_ALPHA = 100
PAUSE_ALPHA_CHANGE_SPEED = 30
FINISHED_ALPHA_CHANGE_SPEED = 0.5
DEFAULT_ALPHA_CHANGE_SPEED = 30

TITLE_FONT_SIZE = 50
DEFAULT_FONT_SIZE = 35

GUI_TEXT_COLOR = THECOLORS['black']
CLOCK_RECT_COLOR = THECOLORS['gray20']
CLOCK_TEXT_COLOR = THECOLORS['gray69']
CLOCK_FONT_SIZE = 35

SELECT_WIDTH = 3
SELECT_ANIMATION_TIME = 0.5
SELECT_LINE_WIDTH = 2
SELECT_ANIMATION_AMP = 10
HOVER_AMP = 10

BALANCED_SPIN_SPEED = 3
FAST_SPIN_SPEED = 1
TANK_ANIMATION_AMP = 5
TANK_ANIMATION_SPEED = 1
TANK_SPIN_SPEED = 1
FERTILE_ANIMATION_AMP = 0.3
FERTILE_ANIMATION_SPEED = 0.3
FERTILE_SPIN_SPEED = 3

BALANCED_POLYGON_SIDES = 3
FAST_POLYGON_SIDES = 3
FERTILE_POLYGON_SIDES = 5
TANK_POLYGON_SIDES = 4
