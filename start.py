from dialog_tree import DialogTree
from gamemanager import GameManager, WIN_WIDTH, WIN_HEIGHT
import pygame
from pygame import *

#WIN_WIDTH = 800
#WIN_HEIGHT = 640
HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0

def begin_game():
	pygame.init()
	screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
	pygame.display.set_caption("Text Adventure!")
	manager = GameManager(screen)
	manager.run_game()

if __name__ == "__main__": begin_game()