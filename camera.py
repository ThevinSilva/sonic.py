import pygame

""" 
camera for this emulation deviates from the original 

"""
class camera(object):
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.rect = pygame.Rect(0,0,width,height)
        self.velocity = pygame.math.Vector2(0, 0)

    def update(self,target):
        self.target = target
        self.rect.move_ip(*self.velocity)


    @staticmethod
    def camera_func(camera, target_rect):
        l, t, _, _ = target_rect
        _, _, w, h = camera
        return pygame.Rect(-l + (896/2), -t + (1280/2), w, h)


    def offset(self):
        return self.rect.topleft