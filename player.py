import pygame

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
        self.movex = (t_f_list[key_input[pygame.K_a]] * -2) + (t_f_list[key_input[pygame.K_d]] * 2)
        self.movey = (t_f_list[key_input[pygame.K_w]] * -2) + (t_f_list[key_input[pygame.K_s]] * 2)

    #Dashing Movement
        if pygame.key.get_mods() & pygame.KMOD_SHIFT and (key_input[pygame.K_w] or key_input[pygame.K_s]) and self.dash_timer<0:
            self.movey *=15
            self.dash_timer = 10*30

        if pygame.key.get_mods() & pygame.KMOD_SHIFT and (key_input[pygame.K_a] or key_input[pygame.K_d]) and self.dash_timer<0:
            self.movex *=15
            self.dash_timer = 10*30
        
        if key_input[pygame.K_a]:
            self.direction = -1
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
    timer=20
    sword_move=0
    def __init__(self,startX,startY,direction):
        super().__init__()
        self.img_left = pygame.image.load("SwordL.png")
        self.img_left =  pygame.transform.scale(self.img_left , (30, 10)).convert_alpha()
        self.img_right = pygame.image.load("SwordR.png")
        self.img_right = pygame.transform.scale(self.img_right , (30, 10)).convert_alpha()
        self.image = self.img_left
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))
        self.direction = direction
        
        if direction==1:
            self.image = self.img_right
            self.mask  = pygame.mask.from_surface(self.image)
        if direction==-1:
            self.image = self.img_left
            self.mask  = pygame.mask.from_surface(self.image)
            
    def update(self,y,x):
        self.timer-=1

        if self.direction ==1:
            speed = 1
        else:
            speed = -1

        if self.timer<=10:
            speed = -speed
            
        self.rect.y = y
        self.rect.x = x
        self.sword_move +=2*speed
        self.rect.x += self.sword_move
        if self.timer==0:
            self.kill()