"""
Map manager.
"""

import os
from Colony import RegularColony
from GUI.Point import Point

EMPTY_COL_FIELD = "EMPTY_COL"
PLAYER_COL_FIELD = "PLAYER_COL"
ENEMY_COL_FIELD = "ENEMY_COL"
NAME_FIELD = "NAME"
N_ENEMIES_FIELD = "N_ENEMIES"

INSTRUCTION_FILENAME = "INSTRUCTIONS.txt"


class MapManager:
    """
    Reads and stores maps.
    """

    def __init__(self):
        self.maps = {}
        self.read_files("\\data\\maps\\")

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
            map_data = dict()
            map_data[NAME_FIELD] = ""
            map_data[N_ENEMIES_FIELD] = 0
            map_data[EMPTY_COL_FIELD] = []
            map_data[ENEMY_COL_FIELD] = []
            map_data[PLAYER_COL_FIELD] = []
            for line in f:
                line = line.strip("\n")
                elements = line.split("=")
                if len(elements) == 2:
                    if elements[0] == NAME_FIELD:
                        map_data[NAME_FIELD] = elements[1]
                    if elements[0] == N_ENEMIES_FIELD:
                        map_data[N_ENEMIES_FIELD] = int(elements[1])
                    else:
                        args = elements[1].split(",")
                        field = ""
                        if elements[0] == EMPTY_COL_FIELD:
                            field = EMPTY_COL_FIELD
                        if elements[0] == ENEMY_COL_FIELD:
                            field = ENEMY_COL_FIELD
                        if elements[0] == PLAYER_COL_FIELD:
                            field = PLAYER_COL_FIELD
                        if not field == "":
                            map_data[field].append(
                                (RegularColony(), int(args[0]), Point(float(args[1]), float(args[2])), float(args[3])))
            self.maps[map_data[NAME_FIELD]] = map_data

    def get_maps(self):
        """
        :return: Stored maps as Dictionary
        :rtype dict
        """
        return self.maps

    def get_maps_array(self):
        """
        :return: Stored maps as Array
        :rtype list
        """
        result = []
        for key in self.maps:
            result.append(self.maps[key])
        return result
