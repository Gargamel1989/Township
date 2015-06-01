'''
Created on May 19, 2015

@author: joep
'''
import pygame
from game.Game import Game

if __name__ == "__main__":
    pygame.init()

    try:
        game = Game()
        
        game.run()
        
    except:
        pygame.quit()
        raise