import pygame
from random import randint
class treasure():
    def __init__(self, screen, image):
        self.screen=screen
        self.image=pygame.image.load(image)
        self.rect=self.image.get_rect()
        self.rect.x=randint(50, 1250)
        self.rect.y=550
        self.treasurewithdiver=False
        self.show=True
    def drawobject(self):
        if self.show==True:
            self.screen.blit(self.image, self.rect)