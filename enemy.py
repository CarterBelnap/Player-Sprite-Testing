import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self,startX,startY,timer,image_left, image_right,width,height):
        super().__init__()
        self.timer = timer
        self.reset = timer
        self.img_left = pygame.image.load(image_left)
        self.img_left =  pygame.transform.scale(self.img_left , (width, height)).convert_alpha()
        self.img_right = pygame.image.load(image_right)
        self.img_right = pygame.transform.scale(self.img_right , (width, height)).convert_alpha()
        self.image = self.img_left
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))

    def move(self,x,y):
       self.rect.x += x
       self.rect.y += y
       
    def track(self,x,y):
        self.timer -=1 
        if self.timer <= 0:
            self.timer = self.reset
        #enemy tracking
            if self.rect.x > x:
                self.move(-1,0) 
            if self.rect.x < x:
                self.move(1,0) 
            if self.rect.y > y:
                self.move(0,-1)
            if self.rect.y < y:
                self.move(0,1)