'''
Created on Jun 1, 2015

@author: joep
'''
from unittest import TestCase
import pygame
from util.rect import are_touching

class RectTest(TestCase):
    
    def test_are_touching(self):
        rect_1 = pygame.Rect(3, 3, 1, 1)
        
        self.assertTrue(are_touching(rect_1, pygame.Rect(2, 3, 1, 1)))
        self.assertTrue(are_touching(rect_1, pygame.Rect(3, 2, 1, 1)))
        self.assertTrue(are_touching(rect_1, pygame.Rect(4, 3, 1, 1)))
        self.assertTrue(are_touching(rect_1, pygame.Rect(3, 4, 1, 1)))
        
        self.assertTrue(are_touching(rect_1, pygame.Rect(1, 3, 2, 1)))
        self.assertTrue(are_touching(rect_1, pygame.Rect(3, 1, 1, 2)))
        self.assertTrue(are_touching(rect_1, pygame.Rect(4, 3, 2, 1)))
        self.assertTrue(are_touching(rect_1, pygame.Rect(3, 4, 1, 2)))
        
        self.assertTrue(are_touching(rect_1, pygame.Rect(1, 2, 3, 1)))
        self.assertTrue(are_touching(rect_1, pygame.Rect(2, 1, 1, 3)))
        self.assertTrue(are_touching(rect_1, pygame.Rect(4, 2, 1, 3)))
        self.assertTrue(are_touching(rect_1, pygame.Rect(1, 4, 3, 1)))
        
        self.assertFalse(are_touching(rect_1, pygame.Rect(2, 2, 1, 1)))
        self.assertFalse(are_touching(rect_1, pygame.Rect(4, 2, 1, 1)))
        self.assertFalse(are_touching(rect_1, pygame.Rect(4, 4, 1, 1)))
        self.assertFalse(are_touching(rect_1, pygame.Rect(2, 4, 1, 1)))
        
        self.assertFalse(are_touching(rect_1, pygame.Rect(1, 1, 4, 1)))
        self.assertFalse(are_touching(rect_1, pygame.Rect(1, 5, 4, 1)))
        self.assertFalse(are_touching(rect_1, pygame.Rect(1, 1, 1, 4)))
        self.assertFalse(are_touching(rect_1, pygame.Rect(5, 1, 1, 4)))
        
        self.assertFalse(are_touching(rect_1, pygame.Rect(3, 1, 4, 1)))
        self.assertFalse(are_touching(rect_1, pygame.Rect(3, 5, 4, 1)))
        self.assertFalse(are_touching(rect_1, pygame.Rect(3, 1, 1, 4)))
        self.assertFalse(are_touching(rect_1, pygame.Rect(5, 3, 1, 4)))