import random

import pygame
class bad_fish():
    def __init__(self, screen, imageL, imageR):
        self.screen=screen
        self.imageL=pygame.image.load(imageL)
        self.imageR=pygame.image.load(imageR)
        self.image=self.imageL
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=random.randint(40, 610)
        self.directionLR=0
        self.distanceLR=0
        self.newdirectionLR=True
        self.directionUD=0
        self.distanceUD=0
        self.newdirectionUD=True
        self.position=False
        self.speed=random.randint(1, 2)
    def drawobject(self):
        self.screen.blit(self.image, self.rect)

    def moveLR(self):
        try:
            if self.newdirectionLR==True:
                self.directionLR=random.randint(1, 2)
                if self.directionLR==1:
                    self.image=self.imageL
                    if self.position==False:
                        self.rect.left=1300
                        self.position=True
                    self.distanceLR=random.randint(0, self.rect.x)
                    self.newdirectionLR=False
                elif self.directionLR==2:
                    self.image=self.imageR
                    if self.position==False:
                        self.rect.right=0
                        self.position=True
                    self.distanceLR=random.randint(self.rect.x, 1300)
                    self.newdirectionLR=False
            else:
                if self.directionLR==1:
                    if self.rect.x>self.distanceLR:
                        self.rect.x-=self.speed
                    else:
                        self.newdirectionLR=True
                elif self.directionLR == 2:
                    if self.rect.x < self.distanceLR:
                        self.rect.x += self.speed
                    else:
                        self.newdirectionLR = True
        except:
            pass

    def moveUD(self):
        try:
            if self.newdirectionUD==True:
                self.directionUD=random.randint(1, 2)
                if self.directionUD==1:
                    if self.directionLR==1:
                        pass
                    elif self.directionLR == 2:
                        pass
                    self.distanceUD=random.randint(0, self.rect.y)
                    self.newdirectionUD=False
                elif self.directionUD==2:
                    self.distanceUD=random.randint(self.rect.y, 650)
                    self.newdirectionUD=False
            else:
                if self.directionUD==1:
                    if self.rect.y > self.distanceUD:
                        self.rect.y-=self.speed
                    else:
                        self.newdirectionUD=True
                elif self.directionUD == 2:
                    if self.rect.y < self.distanceUD:
                        self.rect.y += self.speed
                    else:
                        self.newdirectionUD = True
        except:
            pass