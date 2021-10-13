import pygame
import sys
from scoore import game_score
from random import randint
from setting1 import Settings
from agent_R_M_Dp import agent_R_M_D
from lazer import lazer
from cannon_ball import cannon_ball
from fone import fone_hell
class Hell_jamper_Screen(agent_R_M_D, lazer, cannon_ball, fone_hell):
	def __init__(self):
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.width = self.screen.get_rect().width
		self.settings.height = self.screen.get_rect().height
		self.game_score = game_score(self)
		self.fone_hell = fone_hell(self)
		self.Agent_R_M_D = agent_R_M_D(self)
		self.lazer = lazer(self)
		self.lazer2 = lazer(self)
		self.cannon_ball = cannon_ball(self)
		self.dangNTT = [self.lazer, self.cannon_ball]
		self.gravNTT = [self.cannon_ball, self.Agent_R_M_D]
		self.clock = pygame.time.Clock()
		self.updNTT = [self.fone_hell, self.game_score, self.Agent_R_M_D, self.lazer, self.cannon_ball]
	def run(self):
		while True:
			self._check_events()
			self._update_screen()
			for self.ntt in self.updNTT:
				self.ntt.update()
				self.clock.tick(1000000000000000000)
	def _check_events(self):
		if self.game_score.scorer == 10 and self.game_score.z == 0:
			self.updNTT.append(self.lazer2)
			self.dangNTT.append(self.lazer2)
		for self.ntt in self.dangNTT:
				if self.Agent_R_M_D.rect.colliderect(self.ntt.rect) and self.ntt.act or self.Agent_R_M_D.rect.colliderect(0, 770, 1400, 800):
					self.dethe()
		for self.ntt in self.gravNTT:
			self.ntt.y += self.ntt.grav
			self.ntt.grav += 0.015
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
		self.updNTT = [self.fone_hell, self.game_score, self.Agent_R_M_D, self.lazer, self.cannon_ball]
		self.dangNTT = [self.lazer, self.cannon_ball]
		self.game_score.scorer = -1
		self.game_score.z = 499
		self.Agent_R_M_D.x = self.settings.width / 2
		self.Agent_R_M_D.y = -(self.settings.height) + 800
		self.Agent_R_M_D.grav = 0
		self.Agent_R_M_D.jamp = False
	def _update_screen(self):
		pygame.display.flip()
ai = Hell_jamper_Screen()
ai.run()