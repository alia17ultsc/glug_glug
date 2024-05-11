import pygame

class Bullet():
    def __init__(self, screen, diver):
        self.screen=screen
        self.diver=diver
        self.imageR=pygame.image.load('bulletR.png')
        self.imageL=pygame.image.load('bulletL.png')
        self.image=self.imageL
        self.rect=self.image.get_rect()
        self.rect.x=self.diver.rect.x
        self.rect.y=self.diver.rect.y +60
        self.direction=self.diver.direction
        self.setdirection()
        self.speed=3

    def setdirection(self):
        if self.diver.direction=='right':
            self.image=self.imageR
        else:
            self.image=self.imageL

    def drawobject(self):
        self.screen.blit(self.image, self.rect)

    def move(self):
        if self.direction=='right':
            self.rect.x+=self.speed
        else:
            self.rect.x-=self.speed