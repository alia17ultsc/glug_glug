import random
import pygame, sys
from random import randint
from decoration import item_decor
from diver_maincharacter import diver_
from badfish import bad_fish
from bullet import Bullet
from datetime import datetime
from treasure import treasure



def taketreasure():
    takeonetreasure(chest)
    takeonetreasure(ruby)
    takeonetreasure(pearl)

def takeonetreasure(treasure1):
    print(diver.emptyhands)
    if diver.emptyhands==True:
        if checkcollision(diver, treasure1)==True and treasure1.show==True and treasure1.treasurewithdiver==False:
            diver.emptyhands=False
            treasure1.treasurewithdiver=True
    if treasure1.rect.y<5:
        treasure1.treasurewithdiver=False
        treasure1.show=False
        diver.emptyhands=True

def checkfishkill():
    for onefish in badfishlist.copy():
        for onebullet in bullets.copy():
            if checkcollision(onefish, onebullet)==True:
                badfishlist.remove(onefish)
                bullets.remove(onebullet)

def checkcollision(object1, object2):
    collision=pygame.sprite.collide_mask(object1, object2)
    if collision:
        return True
    else:
        return False
def createbullet():
    global lastshoot
    if shoot==True:
        bullet=Bullet(window, diver)
        bullets.append(bullet)
        lastshoot=datetime.now().second
        print(lastshoot)

lastshoot=0
window=pygame.display.set_mode((1300, 650))
pygame.display.set_caption('Glug Glug')
pygame.display.set_icon(pygame.image.load('fish_right.png'))
sand=item_decor(window, 'sand.png', 0, 350)
diver=diver_(window, 'diver_left.png', 'diver_right.png', 600, 15)
badfishamount=random.randint(4, 7)
badfishlist=[]
bullets=[]
chest=treasure(window, 'chest.png')
ruby=treasure(window, 'ruby.png')
pearl=treasure(window, 'pearl.png')
shoot=False
for i in range(badfishamount):
    badfish_=bad_fish(window, 'evilfishL.png', 'evilfishR.png')
    badfishlist.append(badfish_)
seagrass_=item_decor(window, 'seagrass.png', randint(0, 1300), 300)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                diver.moveL=True
            elif event.key==pygame.K_d:
                diver.moveR=True
            if event.key==pygame.K_w:
                diver.moveUp=True
            elif event.key==pygame.K_s:
                diver.moveDown=True
            if event.key==pygame.K_SPACE:
                shoot=True
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_SPACE:
                shoot=False
            if event.key==pygame.K_a:
                diver.moveL=False
            elif event.key==pygame.K_d:
                diver.moveR=False
            if event.key == pygame.K_w:
                diver.moveUp = False
            elif event.key == pygame.K_s:
                diver.moveDown = False
    window.fill((38, 56, 255))
    sand.drawobject()
    chest.drawobject()
    if chest.treasurewithdiver==True:
        chest.rect=diver.rect
    ruby.drawobject()
    if ruby.treasurewithdiver==True:
        ruby.rect=diver.rect
    pearl.drawobject()
    if pearl.treasurewithdiver==True:
        pearl.rect=diver.rect
    diver.drawobject()
    diver.moveobject()
    for badfish_ in badfishlist:
        badfish_.drawobject()
        badfish_.moveLR()
        badfish_.moveUD()
    seagrass_.drawobject()
    if lastshoot!=datetime.now().second:
        createbullet()
    for bullet in bullets:
        bullet.drawobject()
        bullet.move()
    for onebullet in bullets.copy():
        if onebullet.rect.right<0 or onebullet.rect.left>1300:
            bullets.remove(onebullet)
    checkfishkill()
    taketreasure()
    pygame.display.flip()