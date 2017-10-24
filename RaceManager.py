"""
Race reader.
"""

import os
from Race import Race
from Settings.GeneralSettings import *

RACE_ID_FIELD = "ID"
RACE_NAME_FIELD = "NAME"
RACE_STRENGTH_FIELD = "STRENGTH"
RACE_DEFENSE_FIELD = "DEFENSE"
RACE_SPEED_FIELD = "SPEED"
RACE_REPRODUCTION_TIME_FIELD = "REPRODUCTION_TIME"
RACE_ANIMATION_ID_FIELD = "ANIMATION_ID"
RACE_COLOR_FIELD = "COLOR"
RACE_N_SIDES_FIELD = "N_SIDES"

NULL_RACE_ID = "null_race"

INSTRUCTION_FILENAME = "INSTRUCTIONS.txt"

class RaceManager:
    """
    Reads and stores Races.
    """

    def __init__(self):
        self.races = {}
        self.read_files("\\data\\races\\")

    def read_files(self, sub_folder):
        """
        Loads race files.
        :param sub_folder: Sub folder where the data is
        :type sub_folder: str
        """
        for file in os.listdir(os.getcwd() + sub_folder):
            if file == INSTRUCTION_FILENAME:
                continue
            f = open(os.getcwd() + sub_folder + file)

            race_data = {}
            for line in f:
                line = line.strip("\n")
                elements = line.split("=")
                if len(elements) == 2:
                    race_data[elements[0]] = elements[1]
            try:
                self.races[race_data[RACE_ID_FIELD]] = Race(race_data[RACE_ID_FIELD],
                                                            race_data[RACE_NAME_FIELD],
                                                            race_data[RACE_STRENGTH_FIELD],
                                                            race_data[RACE_DEFENSE_FIELD],
                                                            int(race_data[RACE_SPEED_FIELD]) * GAME_SPEED_FACTOR,
                                                            int(race_data[
                                                                    RACE_REPRODUCTION_TIME_FIELD]) / GAME_SPEED_FACTOR,
                                                            race_data[RACE_ANIMATION_ID_FIELD],
                                                            race_data[RACE_COLOR_FIELD],
                                                            race_data[RACE_N_SIDES_FIELD])

            except KeyError:
                print("Not enough information in file")

    def get_races(self):
        """
        :return: Stored races as Dictionary
        :rtype dict
        """
        return self.races

    def get_races_array(self):
        """
        :return: Stored races as Array
        :rtype list
        """
        result = []
        for key in self.races:
            result.append(self.races[key])
        return result
