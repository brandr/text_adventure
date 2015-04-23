import pygame
from pygame import *

from dialog_tree import DialogTree, MASTER_DIALOG_DATA_MAP, TEXT, NEXT, CHANCE

WIN_WIDTH = 800
WIN_HEIGHT = 640

OPTION_WIDTH = (WIN_WIDTH - 32)/4
OPTION_HEIGHT = 22

WHITE = Color("#FFFFFF")

class GameManager:
	def __init__(self, screen):
		self.screen = screen
		self.timer = pygame.time.Clock()
		self.days = 0
		self.babies = 0
		self.babies_respect = 0
		self.score = 0
		self.dialog_tree = DialogTree(self, MASTER_DIALOG_DATA_MAP)
		self.can_restart = False

	def run_game(self):
		self.title_font = pygame.font.Font('./fonts/FreeSansBold.ttf', 32)
		self.data_font = pygame.font.Font('./fonts/FreeSansBold.ttf', 12)
		self.current_text_font = pygame.font.Font('./fonts/FreeSansBold.ttf', 14)
		self.options_font = pygame.font.Font('./fonts/FreeSansBold.ttf', 16)
		title_image = self.title_font.render("Welcome to the game!", False, WHITE)
		left = right = up = down = False

		self.selector_index = 0
		self.selector = Surface((16, 16))
		self.selector.fill(WHITE)

		bg = Surface((WIN_WIDTH, WIN_HEIGHT))
		
		while 1:
			up = down = left = right = enter = False
			self.screen.blit(bg, (0, 0))
			self.timer.tick(60)
			events = pygame.event.get()
			option_count = self.dialog_tree.option_count()
			self.draw_player_data()
			self.draw_current_text()
			self.draw_options(option_count)
			self.draw_restart_button()
			
			for e in events:
				if e.type == QUIT: return
				if e.type == KEYDOWN and e.key == K_UP: up = True
				if e.type == KEYDOWN and e.key == K_DOWN: down = True
				if e.type == KEYDOWN and e.key == K_LEFT: left = True
				if e.type == KEYDOWN and e.key == K_RIGHT: right = True
				if e.type == KEYDOWN and e.key == K_RETURN: enter = True
			if option_count and up and not down: self.selector_index = (self.selector_index - 1)%option_count
			if option_count and down and not up: self.selector_index = (self.selector_index + 1)%option_count
			if enter: 
				self.dialog_tree.make_selection(self.selector_index)
				self.selector_index = 0
			pygame.display.update()

	def draw_player_data(self):
		days_image = self.data_font.render("Days: " + str(self.days), False, WHITE)
		babies_image = self.data_font.render("Babies: " + str(self.babies), False, WHITE)
		babies_respect_image = self.data_font.render("Babies' Respect: " + str(self.babies_respect), False, WHITE)
		score_image = self.data_font.render("Score: " + str(self.score), False, WHITE)
		self.screen.blit(days_image, (8, 8))
		self.screen.blit(babies_image, (8, 24))
		self.screen.blit(babies_respect_image, (8, 40))
		self.screen.blit(score_image, (8, 56))

	def draw_current_text(self):
		index = 0
		current_text_set = self.dialog_tree.get_current_text()
		for t in current_text_set:
			self.screen.blit(self.current_text_font.render(t, False, WHITE), (16, 100 + index*20))
			index += 1

	def draw_options(self, option_count):
		options = self.dialog_tree.get_current_options(self.dialog_tree.get_current_event_map())
		if not options: return
		options_text_set = []
		for o in options: options_text_set.append(o[TEXT])
		options_text_images = self.draw_option_text_images(options_text_set)
		i = 0
		for o in options_text_images:
			self.screen.blit(o, (32, 400 + i*OPTION_HEIGHT))
			i += 1
		if option_count: self.screen.blit(self.selector, (8, 400 + self.selector_index*OPTION_HEIGHT))

	def draw_option_text_images(self, option_text_set):
		image_set = []
		for t in option_text_set: image_set.append(self.options_font.render(t, False, WHITE))
		return image_set

	def draw_restart_button(self):
		if not self.can_restart: return
		restart_image = self.options_font.render("Restart", False, WHITE)
		self.screen.blit(restart_image, (32, 400))
		self.screen.blit(self.selector, (8, 400))

	def add_restart_button(self):
		self.can_restart = True

	def restart(self):
		self.days = 0
		self.babies = 0
		self.babies_respect = 0
		self.score = 0
		self.dialog_tree = DialogTree(self, MASTER_DIALOG_DATA_MAP)
		self.can_restart = False
#"You decide to stay the night, but just before you go into the tree trunk, a snake bursts out of the trunk and poisons you. GAME OVER."