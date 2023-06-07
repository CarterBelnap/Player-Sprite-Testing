import pygame

#ADD FLIPPING MODEL
#ADD ATTACKING WT SWORD

class Player(pygame.sprite.Sprite):
    #Init Sprite  
    dash_timer = 10*30
    direction = 1
    attack = 1
    def __init__(self,startX,startY):
        super().__init__()
        self.img_left = pygame.image.load("images (3).png")
        self.img_left =  pygame.transform.scale(self.img_left , (30, 30)).convert_alpha()
        self.img_right = pygame.image.load("images.png")
        self.img_right = pygame.transform.scale(self.img_right , (30, 30)).convert_alpha()
        self.image = self.img_left
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))
    #Basic Movement
    def move(self):
        self.dash_timer -=1
        global key_input, t_f_list
        t_f_list = {True : 1, False: 0}
        key_input = pygame.key.get_pressed() 
        self.movex = (t_f_list[key_input[pygame.K_a]] * -4) + (t_f_list[key_input[pygame.K_d]] * 4)
        self.movey = (t_f_list[key_input[pygame.K_w]] * -4) + (t_f_list[key_input[pygame.K_s]] * 4)

    #Dashing Movement
        if pygame.key.get_mods() & pygame.KMOD_SHIFT and (key_input[pygame.K_w] or key_input[pygame.K_s]) and self.dash_timer<0:
            self.movey *=15
            self.dash_timer = 10*30

        if pygame.key.get_mods() & pygame.KMOD_SHIFT and (key_input[pygame.K_a] or key_input[pygame.K_d]) and self.dash_timer<0:
            self.movex *=15
            self.dash_timer = 10*30
        
        if key_input[pygame.K_a]:
            self.direction = 2
            self.image = self.img_right
            self.mask  = pygame.mask.from_surface(self.image)
            
        if key_input[pygame.K_d]:
            self.direction = 1
            self.image = self.img_left
            self.mask  = pygame.mask.from_surface(self.image)
            
        self.rect.y += self.movey
        self.rect.x += self.movex 
        
    #Object Collision
    def collide(self):
        self.rect.x -= self.movex
        self.rect.y -= self.movey

class Sword(pygame.sprite.Sprite):

    def __init__(self,startX,startY,direction):
        super().__init__()
        self.img_left = pygame.image.load("sword2.png")
        self.img_left =  pygame.transform.scale(self.img_left , (30, 30)).convert_alpha()
        self.img_right = pygame.image.load("sword.png")
        self.img_right = pygame.transform.scale(self.img_right , (30, 30)).convert_alpha()
        self.image = self.img_left
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))
        
        if direction==1:
            self.image = self.img_right
            self.mask  = pygame.mask.from_surface(self.image)
        if direction==2:
            self.image = self.img_left
            self.mask  = pygame.mask.from_surface(self.image)
            
    def update(self,speed,location):
        self.rect.x+=speed*location