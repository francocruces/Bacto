"""
Sound driver.
"""

import pygame


class SoundDriver:
    """
    Sound driver. Takes sound resources and plays them.
    """
    def __init__(self):
        pygame.mixer.init(48000, 16)
        pygame.mixer.music.load("res/think_twice.wav")
        pygame.mixer.music.play(-1)

        self.taken = pygame.mixer.Sound("res/Sounds/taken.wav")
        self.move_selection = pygame.mixer.Sound("res/Sounds/move_selection.wav")
        self.select = pygame.mixer.Sound("res/Sounds/taken.wav")

    def play_select(self):
        """
        Play sound for selection.
        """
        self.select.play()

    def play_move_selection(self):
        """
        Play sound for selection moving.
        """
        self.move_selection.play()

    def play_taken(self):
        """
        Play sound for taken colony.
        """
        self.taken.play()
