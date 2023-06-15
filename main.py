import pygame, sys
from player import *
from enemy import *
pygame.init
fps = 60

fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

pygame.display.set_caption("Player Testing")
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
player_group=pygame.sprite.Group()
sword_group=pygame.sprite.Group()
enemy_group=pygame.sprite.Group()
player_sprite = Player(100,100)
enemy_sprite = Enemy(300,300,3,"PlayerL.png","PlayerR.png",30,40,100)
player_group.add(player_sprite)
enemy_group.add(enemy_sprite)



def attack():
    if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
        sword_sprite = Sword(player_sprite.rect.x+player_sprite.direction*15,player_sprite.rect.y+10,player_sprite.direction)
        sword_group.add(sword_sprite)

def display():
    window.fill(0x000000)
    player_group.draw(window)
    enemy_group.draw(window)
    sword_group.draw(window)
while True:
    display()
    for event in pygame.event.get():
    # if user  QUIT then the screen will close
        if event.type == pygame.QUIT:
            sys.exit()
    player_sprite.move()
    sword_group.update(player_sprite.rect.y+10,player_sprite.rect.x+player_sprite.direction*15,enemy_group)
    if len(sword_group)<1:
        attack()
    enemy_sprite.track(player_sprite.rect.x,player_sprite.rect.y)  
    enemy_group.update(player_group)
            
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw