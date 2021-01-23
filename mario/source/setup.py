import pygame
from . import constants as C


def init_game():
    pygame.init()
    pygame.display.set_mode(C.SCREEN_SIZE)