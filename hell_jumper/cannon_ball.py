import pygame
import time
from random import randint
class cannon_ball:
    """A class to manage the ship."""
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # Load the ship image and get its rect.
        self.image = pygame.image.load(('arts/cannonball.png'))
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image.set_colorkey(0, 0)
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(center=(self.settings.width, self.settings.height / 2))
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.ad = 0
        self.z = 0
        self.act = True
    def update(self):
        if self.rect.bottom >= self.screen_rect.bottom:
            self.y = randint(0, 300)
            self.x = 1200
        if self.rect.bottom <= self.screen_rect.bottom:
            self.x -= 4
            self.y += self.ad
            self.ad += 0.02
        if self.rect.bottom >= self.screen_rect.bottom:
            self.ad = 0
        self.rect.x = self.x
        self.rect.y = self.y
        self.screen.blit(self.image, self.rect)
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
