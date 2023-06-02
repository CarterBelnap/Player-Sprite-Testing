import pygame

#ADD FLIPPING MODEL
#ADD ATTACKING WT SWORD


class Player(pygame.sprite.Sprite):
    #Init Sprite  
    dash_timer = 10*30
    def __init__(self,startX,startY,width,height,load_path):
        super().__init__()
        img_load = pygame.image.load(load_path)
        img_copy = img_load.copy()
        img_flip = pygame.transform.flip(img_copy, True, False)
        self.image = pygame.transform.scale(img_load , (width, height)).convert_alpha()
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
            
        self.rect.y += self.movey
        self.rect.x += self.movex 
    #Flip Character Model   
    """def flip(self):
        if t_f_list[key_input[pygame.K_a]]:"""
            
                    

        
    #Object Collision
    def collide(self):
        self.rect.x -= self.movex
        self.rect.y -= self.movey

    #def attack(self):
