import pygame
import sys
from random import randint
from setting1 import Settings
from agent_R_M_Dp import agent_R_M_D
from lazer import lazer
from cannon_ball import cannon_ball
from fone import fone_hell
class Hell_jamper_Screen(agent_R_M_D, lazer, cannon_ball, fone_hell):
	"""docstring for ClassName"""
	def __init__(self):
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.width = self.screen.get_rect().width
		self.settings.height = self.screen.get_rect().height
		self.fone_hell = fone_hell(self)
		self.Agent_R_M_D = agent_R_M_D(self)
		self.lazer = lazer(self)
		self.cannon_ball = cannon_ball(self)
		self.NTT = (self.lazer, self.cannon_ball) 
	def run(self):
		while True:
			self._check_events()
			self._update_screen()
			self.fone_hell.update()
			self.Agent_R_M_D.update()			
			self.lazer.update()
			self.cannon_ball.update()
	def _check_events(self):
		if self.Agent_R_M_D.rect.bottom > self.Agent_R_M_D.screen_rect.bottom:
			self.dethe()
		for self.ntt in self.NTT:
				if self.Agent_R_M_D.rect.colliderect(self.ntt.rect) and self.ntt.act:
					self.dethe()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self.event_KEYDOWN(event)
			elif event.type == pygame.KEYUP:
				self.event_KEYUP(event)
	def event_KEYUP(self, event):
		if event.key == pygame.K_RIGHT:
			self.Agent_R_M_D.moving_right = False
		if event.key == pygame.K_LEFT:
			self.Agent_R_M_D.moving_left = False
		if event.key == pygame.K_UP:
			self.Agent_R_M_D.jamp = False
		if event.key == pygame.K_DOWN:
			self.Agent_R_M_D.speeds = False
	def event_KEYDOWN(self, event):
		if event.key == pygame.K_RIGHT:
			self.Agent_R_M_D.moving_right = True
		if event.key == pygame.K_LEFT:
			self.Agent_R_M_D.moving_left = True
		if event.key == pygame.K_UP:
			self.Agent_R_M_D.jamp = True
		if event.key == pygame.K_DOWN:
			self.Agent_R_M_D.speeds = True
		if event.key == pygame.K_q:
			sys.exit()	
	def dethe(self):
		self.Agent_R_M_D.x = self.settings.width / 2
		self.Agent_R_M_D.y = -(self.settings.height) + 800
		self.settings.grav = 0
		self.Agent_R_M_D.jamp = False
	def _update_screen(self):
		pygame.display.flip()
ai = Hell_jamper_Screen()
ai.run()