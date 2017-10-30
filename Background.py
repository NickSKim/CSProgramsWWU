import pygame, math, random, os
import time


class Back(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        #self.screen = screen
        #self.bg_color = bg_color
        #self.clock = pygame.time.Clock()
