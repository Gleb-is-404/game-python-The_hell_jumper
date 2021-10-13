import pygame
from random import randint
class lazer:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.imwork('arts/lazer_vermilion.png')
        self.rect = self.image.get_rect(center=(self.settings.width / 2, self.settings.height / 2))
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.z = 0
        self.act = False
    def imwork(self, name):
        self.image = pygame.image.load((name))
        self.image = pygame.transform.scale(self.image, (1400, 80))
        self.image.set_colorkey(0, 0)
    def update(self):
        if self.z == 100:
            self.imwork('arts/lazer_vermilion_prepared.png')
            self.act = False
            self.rect.y = randint(0, 700) 
        if self.z == 350:
            self.imwork('arts/lazer_vermilion.png')
            self.act = True
        if self.z == 400:
               self.z = 0
        self.z += 1
        self.screen.blit(self.image, self.rect)