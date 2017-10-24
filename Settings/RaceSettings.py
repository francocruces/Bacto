"""
Settings for races. Contains their stats and names.
"""

from Settings.GeneralSettings import *

# Factors for global changes
SPEED_FACTOR = 1 * GAME_SPEED_FACTOR
REPRODUCTION_TIME_FACTOR = 1 / GAME_SPEED_FACTOR
STRENGTH_FACTOR = 1
DEFENSE_FACTOR = 1

# Default stats
DEFAULT_SPEED = 10 * SPEED_FACTOR
DEFAULT_REPRODUCTION_TIME = 10 * REPRODUCTION_TIME_FACTOR
DEFAULT_STRENGTH = 10 * STRENGTH_FACTOR
DEFAULT_DEFENSE = 10 * DEFENSE_FACTOR

# Stats of NPCs
NULL_ID = "null_race"
NULL_SPEED = 10 * SPEED_FACTOR
NULL_REPRODUCTION_TIME = 180 * REPRODUCTION_TIME_FACTOR
NULL_STRENGTH = 10 * STRENGTH_FACTOR
NULL_DEFENSE = 10 * DEFENSE_FACTOR
NULL_NAME = "No Race"
NULL_COLOR = "black"
NULL_ANIMATION_ID = "spin"
NULL_SIDES = 3

# Stats of Balanced Race
BALANCED_SPEED = 10 * SPEED_FACTOR
BALANCED_REPRODUCTION_TIME = 10 * REPRODUCTION_TIME_FACTOR
BALANCED_STRENGTH = 10 * STRENGTH_FACTOR
BALANCED_DEFENSE = 10 * DEFENSE_FACTOR
BALANCED_NAME = "Balanced Race"

# Stats of Fast Race
FAST_SPEED = 16 * SPEED_FACTOR
FAST_REPRODUCTION_TIME = 10 * REPRODUCTION_TIME_FACTOR
FAST_STRENGTH = 12 * STRENGTH_FACTOR
FAST_DEFENSE = 6 * DEFENSE_FACTOR
FAST_NAME = "Fast Race"

# Stats of Fertile Race
FERTILE_SPEED = 7 * SPEED_FACTOR
FERTILE_REPRODUCTION_TIME = 7 * REPRODUCTION_TIME_FACTOR
FERTILE_STRENGTH = 8 * STRENGTH_FACTOR
FERTILE_DEFENSE = 11 * DEFENSE_FACTOR
FERTILE_NAME = "Fertile Race"

# Stats of Tank Race
TANK_SPEED = 7 * SPEED_FACTOR
TANK_REPRODUCTION_TIME = 12 * REPRODUCTION_TIME_FACTOR
TANK_STRENGTH = 14 * STRENGTH_FACTOR
TANK_DEFENSE = 14 * DEFENSE_FACTOR
TANK_NAME = "Tank Race"