import pygame
import time
from random import randint
from setting1 import Settings
from agent_R_M_Dp import agent_R_M_D
class play_batomme:
    """A class to manage the ship."""
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.Agent_R_M_D = agent_R_M_D(self)
        # Load the ship image and get its rect.
        self.image = pygame.image.load(('arts/bat_play.png'))
        self.image = pygame.transform.scale(self.image, (180, 60))
        self.image.set_colorkey(0, 0)
        self.rect = self.image.get_rect(center=(self.settings.width / 2, self.settings.height / 2))
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        settings = Settings()
        # Start each new ship at the bottom center of the screen.
        self.act = False
    def update(self):
        if self.act:    
            self.screen.blit(self.image, self.rect)
            self.Agent_R_M_D.x = self.settings.width / 2
            self.Agent_R_M_D.y = -(self.settings.height) + 800

