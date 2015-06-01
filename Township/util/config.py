'''
Created on May 30, 2015

@author: joep
'''
import os

RANDOM_SEED = 1

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
DB_DIR = os.path.join(ASSETS_DIR, 'db')
SAVE_DIR = os.path.join(BASE_DIR, 'savegames')
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)


# Graphic config
SCREEN_SIZE = (1024, 768)

TILE_DIMENSION = 32

