import pygame
class diver_():
    def __init__(self, screen, imageL, imageR, x, y):
        self.screen=screen
        self.imageL=pygame.image.load(imageL)
        self.imageR = pygame.image.load(imageR)
        self.image = self.imageL
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.moveL=False
        self.moveR=False
        self.moveUp=False
        self.moveDown=False
        self.speed=2
        self.direction='right'
        self.emptyhands=True
    def drawobject(self):
        self.screen.blit(self.image, self.rect)
    def moveobject(self):
        if self.moveL==True:
            self.image=self.imageL
            self.rect.x-=self.speed
            self.direction='left'
            if self.rect.right<1:
                self.rect.centerx=self.screen.get_rect().right
        elif self.moveR==True:
            self.image=self.imageR
            self.rect.x+=self.speed
            self.direction='right'
            if self.rect.left>1299:
                self.rect.centerx=0
        if self.moveUp==True:
            self.rect.y-=self.speed
            if self.rect.top<0:
                self.rect.y+=self.speed
        elif self.moveDown==True:
            self.rect.y+=self.speed
            if self.rect.bottom>650:
                self.rect.y-=self.speed