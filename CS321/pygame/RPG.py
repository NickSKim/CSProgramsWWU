import pygame, math, random, os
#from Character import Charmove
#from Menu import Main
#from "Local file name" import "Class name"

pygame.init()
screen = pygame.display.set_mode((700, 600))
pygame.display.flip()
done = True

pygame.display.set_caption('Title goes here')

background_colour = (255,30,200)
screen.fill(background_colour)


class Main():
    def __init__(self, screen, bg_color=(0,0,0)):
 
        self.screen = screen
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()

        while done:
                # Limit frame speed to 50 FPS
                self.clock.tick(50)
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                done = False
 
        # Redraw the background
        self.screen.fill(self.bg_color)
        pygame.display.flip()
 
#if __name__ == "__main__":
    # Creating the screen
    #screen = pygame.display.set_mode((640, 480), 0, 32)
    #pygame.display.set_caption('Game Menu')
    #gm = GameMenu(screen)
    #gm.run()




pygame.quit()
