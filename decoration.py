import pygame
class item_decor():
    def __init__(self, screen, image, x, y):
        self.screen=screen
        self.image=pygame.image.load(image)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def drawobject(self):
        self.screen.blit(self.image, self.rect)