import pygame
import sys
from setting1 import Settings
class game_score():
	def __init__(self, ai_game):
		self.screen = ai_game.screen
		self.image1 = pygame.image.load(('NUMBER/number0.png'))
		self.image1 = pygame.transform.scale(self.image1, (60, 60))
		self.image1.set_colorkey(0, 0)
		self.rect1 = self.image1.get_rect(center=(120, 60))
		self.image2 = pygame.image.load(('NUMBER/number0.png'))
		self.image2 = pygame.transform.scale(self.image2, (60, 60))
		self.image2.set_colorkey(0, 0)
		self.rect2 = self.image2.get_rect(center=(40, 60))
		self.x1 = float(self.rect1.x)
		self.y1 = float(self.rect1.y)
		self.x2 = float(self.rect2.x)
		self.y2 = float(self.rect2.y)
		self.z = 0
		self.scorer = 0
		self.list_of_number = ['NUMBER/number0.png', 'NUMBER/number1.png', 'NUMBER/number2.png', 'NUMBER/number3.png', 'NUMBER/number4.png', 'NUMBER/number5.png', 'NUMBER/number6.png', 'NUMBER/number7.png', 'NUMBER/number8.png', 'NUMBER/number9.png']
	def imwork1(self, name):
		self.image1 = pygame.image.load((name))
		self.image1 = pygame.transform.scale(self.image1, (60, 60))
		self.image1.set_colorkey(0, 0)
	def imwork2(self, name):
		self.image2 = pygame.image.load((name))
		self.image2 = pygame.transform.scale(self.image2, (60, 60))
		self.image2.set_colorkey(0, 0)
	def update(self):
		self.z += 1
		if self.z == 500:
			self.scorer += 1
			self.z = 0
			self.imwork1(self.list_of_number[self.scorer%10])
			self.imwork2(self.list_of_number[self.scorer//10]) 
		self.screen.blit(self.image1, self.rect1)
		self.screen.blit(self.image2, self.rect2)      