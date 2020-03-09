import pygame

'''Bottom Vertical sensor lines '''
class sensor_A(pygame.sprite.Sprite):

    def __init__(self,posx,posy,player):
        super().__init__()
        self.player = player
        self.height = 80
        self.width = 2
        self.rect =  pygame.Rect((self.player.rect.x + 64, self.player.rect.y + 128), (self.width, self.height)).clamp(self.player)
    def draw(self, surface):
        self.surface = surface
        return pygame.draw.rect(surface,(  0, 255,   0) ,self.rect)

class sensor_B(pygame.sprite.Sprite):

    def __init__(self,posx,posy,player):
        super().__init__()
        self.player = player
        self.height = 80
        self.width = 2
        self.rect =  pygame.Rect((self.player.rect.x + 128, self.player.rect.y + 128), (self.width, self.height)).clamp(self.player)
    def draw(self, surface):
        self.surface = surface
        return pygame.draw.rect(surface,(  0, 255,   255) ,self.rect)



''' Horizontal sensor lines '''
class sensor_C(pygame.sprite.Sprite):
    def __init__(self,posx,posy,player):
        super().__init__()
        self.player = player
        self.height = 2
        self.width =  40
        self.rect =  pygame.Rect((self.player.rect.centerx - 41, self.player.rect.y + 128), (self.width, self.height)).clamp(self.player)
    def draw(self, surface):
        self.surface = surface
        return pygame.draw.rect(surface,(  255, 0,   255) ,self.rect)
    def floor_mode(self):
        self.rect.move_ip(0 ,16)


class sensor_D(pygame.sprite.Sprite):
    def __init__(self,posx,posy,player):
        super().__init__()
        self.player = player
        self.height = 2
        self.width =  40
        self.posx = posx
        self.posy = posy + 64
        self.rect =  pygame.Rect((self.player.rect.centerx, self.player.rect.y + 128), (self.width, self.height)).clamp(self.player)
    def draw(self, surface):
        self.surface = surface
        return pygame.draw.rect(surface,(  255, 0,   0) ,self.rect)

    def floor_mode(self):
        self.rect.move_ip(0 ,16)


'''Top Vertical sensor lines '''
class sensor_E(pygame.sprite.Sprite):

    def __init__(self,posx,posy,player):
        super().__init__()
        self.player = player
        self.height = 80
        self.width = 2
        self.posx = posx
        self.posy = posy
        self.rect =  pygame.Rect((self.player.rect.x + 64, self.player.rect.y + 64 - 16), (self.width, self.height)).clamp(self.player)
    def draw(self, surface):
        self.surface = surface
        return pygame.draw.rect(surface,(  100, 0,   255) ,self.rect)



class sensor_F(pygame.sprite.Sprite):

    def __init__(self,posx,posy,player):
        super().__init__()
        self.player = player
        self.height = 80
        self.width = 2
        self.posx = posx
        self.posy = posy
        self.rect =  pygame.Rect((self.player.rect.x + 128, self.player.rect.y + 64 - 16), (self.width, self.height)).clamp(self.player)
    def draw(self, surface):
        self.surface = surface
        return pygame.draw.rect(surface,(  255, 255,   0) ,self.rect)

