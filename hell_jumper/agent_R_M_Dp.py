import pygame
import time
class agent_R_M_D:
    """A class to manage the ship."""
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # Load the ship image and get its rect.
        self.image = pygame.image.load(('arts/agent.R.M.D.png'))
        self.image = pygame.transform.scale(self.image, (70, 140))
        self.image.set_colorkey(0, 0)
        self.rect = self.image.get_rect(center=(self.settings.width / 2, self.settings.height * 2))
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.gravety = True
        self.jamp = False
        self.speeds = False
    def update(self):
        if self.moving_left and self.rect.left >= self.screen_rect.left:
            self.x -= self.settings.speed
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.x += self.settings.speed
        if self.jamp and self.rect.top >= self.screen_rect.top:
            self.settings.grav = -2
        if self.rect.top == self.screen_rect.top:
            self.jamp = False
            self.settings.grav = 1
        self.rect.x = self.x
        self.rect.y = self.y
        if self.speeds:
            self.settings.grav += 0.02
            self.settings.grav = round(self.settings.grav, 2)
        if self.gravety == True:
            self.y += self.settings.grav
            if self.settings.grav < 4:
                self.settings.grav += 0.01
                self.settings.grav = round(self.settings.grav, 2)
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)