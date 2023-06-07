import pygame, sys
from player import *
pygame.init
fps = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

pygame.display.set_caption("Player Testing")
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
player_group=pygame.sprite.Group()
sword_group=pygame.sprite.Group()
player_sprite = Player(100,100)
player_group.add(player_sprite)


def attack(): 
    if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
        sword_sprite = Sword(player_sprite.rect.x,player_sprite.rect.y,player_sprite.direction)
        sword_group.add(sword_sprite)
   
        

        
        
        
def display():
    window.fill(0x000000)
    player_group.draw(window)
while True:
    display()
    for event in pygame.event.get():
        # if user  QUIT then the screen will close
          if event.type == pygame.QUIT:
              sys.exit()
    player_sprite.move()
    sword_sprite.update(5,player_sprite.rect.x)
    attack()
    
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw