import pygame

class Enemy(pygame.sprite.Sprite):

    def __init__(self,startX,startY):
        super().__init__()
        self.img_left = pygame.image.load("PlayerL.png")
        self.img_left =  pygame.transform.scale(self.img_left , (30, 30)).convert_alpha()
        self.img_right = pygame.image.load("PlayerR.png")
        self.img_right = pygame.transform.scale(self.img_right , (30, 30)).convert_alpha()
        self.image = self.img_left
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))
    #Basic Movement
    def track(self):
        
        
