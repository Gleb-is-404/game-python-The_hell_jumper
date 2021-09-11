import pygame
import time
from random import randint
from setting1 import Settings
class lazer:
    """A class to manage the ship."""
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # Load the ship image and get its rect.
        self.image = pygame.image.load(('arts/lazer_vermilion.png'))
        self.image = pygame.transform.scale(self.image, (1400, 80))
        self.image.set_colorkey(0, 0)
        self.rect = self.image.get_rect(center=(self.settings.width / 2, self.settings.height / 2))
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        settings = Settings()
        # Start each new ship at the bottom center of the screen.
        self.z = 0
        self.act = False
    def update(self):
        if self.z == 100:
            self.image = pygame.image.load(('arts/lazer_vermilion_prepared.png'))
            self.image = pygame.transform.scale(self.image, (1400, 80))
            self.image.set_colorkey(0, 0)
            self.act = False
            self.rect.y = randint(0, 700) 
        if self.z == 350:
            self.image = pygame.image.load(('arts/lazer_vermilion.png'))
            self.image = pygame.transform.scale(self.image, (1400, 80))
            self.image.set_colorkey(0, 0)
            self.act = True
        if self.z == 400:
               self.z = 0
        self.z += 1
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
