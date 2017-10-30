import pygame, math, random, os
import time
from Background import Back
from Menu import GameMenu
#from "Local file name" import "Class name"


def main():
    pygame.init()
    board = pygame.image.load("/home/kimn9/CS321/pygame/images/Chess_Board.png")
    screen = pygame.display.set_mode((700, 600))
    done = True
    picture = pygame.image.load("/home/kimn9/CS321/pygame/images/rename.png")
    bg = picture.get_rect()
    #chess = pygame.transform.scale(board) #board.get_rect()
    #background = pygame.image.load("/home/kimn9/CS321/pygame/images/rename.png")
    #size = (width, height) = picture.get_size()
    #screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Adventure RPG')

    #background_colour = (255,30,200)
    #screen.fill(background_colour)
    #scale = 3
    #size = scale*16
    #world = pygame.Surface((500*scale, 500*scale))
    #screensize = (320*scale, 240*scale)
    #screen2 = pygame.display.set_mode(screensize)
    #def __init__(self, screen, bg_color=(0,0,0)):
    
    #self.screen = screen
    #self.bg_color = bg_color
    #self.clock = pygame.time.Clock()
    #gm = GameMenu(screen)
    #gm.run()

    while done:
        
        # Limit frame speed to 50 FPS
        #self.clock.tick(50)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
            #chess = chess.move(speed)
            #if chess.left < 0 or chess.right > width:
                #speed[0] = -speed[0]
            #if chess.top < 0 or chess.bottom > height:
                #speed[1] = -speed[1]
            screen.fill([255, 255, 255])
            screen.blit(picture, [700, 600])
            screen.blit(board, [500, 500])
            pygame.display.update()
        # Redraw the background
        #self.screen.fill(self.bg_color)
    pygame.display.flip()
    
    pygame.quit()
 
#if __name__ == "__main__":
    # Creating the screen
    #screen = pygame.display.set_mode((640, 480), 0, 32)
    #pygame.display.set_caption('Game Menu')
    

if __name__ == "__main__":
    try:
        main()
    finally:
        pygame.quit()
        



