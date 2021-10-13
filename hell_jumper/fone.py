import pygame
class fone_hell:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load(('arts/Hell.png'))
        self.image = pygame.transform.scale(self.image, (1400, 800))
        self.rect = self.image.get_rect(center=(self.settings.width / 2, 400))
    def update(self):
        self.screen.blit(self.image, self.rect)