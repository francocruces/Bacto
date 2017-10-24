"""
Menus for the game.
"""
from GUI.Menu.Menu import Menu
from GUI.Menu.MenuHandler import *
from GUI.Menu.MenuItem import *


COLONY_AMOUNT_MIN = 1
COLONY_AMOUNT_MAX = 30
ENEMY_AMOUNT_MIN = 1
ENEMY_AMOUNT_MAX = 3


def MAIN_MENU(driver):
    menu = Menu(driver)
    label = Label(menu, "BACTO", 130, False)
    author = Label(menu, "Franco Cruces'", 50, False)
    start_button_1 = Button(menu, NextMenuHandler(driver, SET_RANDOM_GAME), "Start Random Game")
    start_button_2 = Button(menu, NextMenuHandler(driver, LOAD_MAP), "Load a custom map")
    separator1 = Label(menu, "", 20)
    separator2 = Label(menu, "", 20)
    separator3 = Label(menu, "", 20)
    exit_button = Button(menu, QuitGameHandler(driver), "Exit")

    menu.insert_item(author)
    menu.insert_item(separator3)
    menu.insert_item(label)
    menu.insert_item(separator1)
    menu.insert_item(start_button_1)
    menu.insert_item(start_button_2)
    menu.insert_item(separator2)
    menu.insert_item(exit_button)
    menu.set_selection(3)
    return menu


def SET_RANDOM_GAME(driver):
    menu = Menu(driver)
    label = Label(menu, "RANDOM GAME SETTINGS", 60, True)

    race_set = Setting(menu, NullHandler(), "")
    races = driver.get_races()
    for key in races:
        if not key == "null_race":
            race_option = PlayerRaceOption(driver, race_set, races[key])
            race_set.insert_option(race_option)

    colony_amount = Setting(menu, NullHandler(), "Empty colonies: ")
    enemy_amount = Setting(menu, NullHandler(), "Enemies: ")

    for i in range(COLONY_AMOUNT_MIN, COLONY_AMOUNT_MAX + 1):
        colony_amount_option = ColonyAmount(driver, colony_amount, i)
        colony_amount.insert_option(colony_amount_option)

    for i in range(ENEMY_AMOUNT_MIN, ENEMY_AMOUNT_MAX + 1):
        enemy_amount_option = EnemyAmount(driver, enemy_amount, i)
        enemy_amount.insert_option(enemy_amount_option)

    colony_amount.select_option(21)
    enemy_amount.select_option(0)

    separator1 = Label(menu, "", 20)
    separator2 = Label(menu, "", 20)

    start_button = Button(menu, StartGameHandler(driver), "Start Game")
    main_menu = Button(menu, NextMenuHandler(driver, MAIN_MENU), "Go to main menu")

    menu.insert_item(label)
    menu.insert_item(separator1)
    menu.insert_item(race_set)
    menu.insert_item(colony_amount)
    menu.insert_item(enemy_amount)
    menu.insert_item(separator2)
    menu.insert_item(start_button)
    menu.insert_item(main_menu)
    menu.set_selection(1)
    return menu


def LOAD_MAP(driver):
    menu = Menu(driver)
    label = Label(menu, "LOAD CUSTOM MAP", 60, True)

    race_set = Setting(menu, NullHandler(), "Race: ")
    races = driver.get_races()
    for key in races:
        if not key == "null_race":
            race_option = PlayerRaceOption(driver, race_set, races[key])
            race_set.insert_option(race_option)

    map_set = Setting(menu, NullHandler(), "Map: ")
    maps = driver.get_maps()
    for key in maps:
        map_option = MapToLoadOption(driver, map_set, maps[key])
        map_set.insert_option(map_option)

    separator1 = Label(menu, "", 20)
    separator2 = Label(menu, "", 20)

    start_button = Button(menu, StartCustomMapHandler(driver), "Start Game")
    main_menu = Button(menu, NextMenuHandler(driver, MAIN_MENU), "Go to main menu")

    menu.insert_item(label)
    menu.insert_item(separator1)
    menu.insert_item(race_set)
    menu.insert_item(map_set)
    menu.insert_item(separator2)
    menu.insert_item(start_button)
    menu.insert_item(main_menu)

    menu.set_selection(2)
    return menu


def MATCH_FINISHED_MENU(driver, winning_race):
    menu = Menu(driver)
    label0 = Label(menu, " ", 60, True)
    label = Label(menu, "MATCH FINISHED", 60, True)
    label2 = Label(menu, "Winner: " + str(winning_race), 40, False)
    label3 = Label(menu, " ", 60, True)
    new_match = Button(menu, NextMenuHandler(driver, SET_RANDOM_GAME), "Start new match")
    main_menu = Button(menu, NextMenuHandler(driver, MAIN_MENU), "Go to main menu")

    menu.insert_item(label0)
    menu.insert_item(label)
    menu.insert_item(label2)
    menu.insert_item(label3)
    menu.insert_item(new_match)
    menu.insert_item(main_menu)

    menu.set_selection(4)
    return menu


def PAUSE_MENU(driver):
    menu = Menu(driver)
    label0 = Label(menu, "", 60, False)
    label = Label(menu, "GAME PAUSED", 60, True)
    label2 = Label(menu, "", 60, False)
    resume_button = Button(menu, UnPauseHandler(driver), "Resume")
    new_match = Button(menu, NextMenuHandler(driver, SET_RANDOM_GAME), "Start new match")
    main_menu = Button(menu, NextMenuHandler(driver, MAIN_MENU), "Go to main menu")

    menu.insert_item(label0)
    menu.insert_item(label)
    menu.insert_item(label2)
    menu.insert_item(resume_button)
    menu.insert_item(new_match)
    menu.insert_item(main_menu)

    menu.set_selection(2)
    return menu
