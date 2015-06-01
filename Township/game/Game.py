# -*- coding: utf-8 -*-
'''
Created on May 19, 2015

@author: joep
'''
from game.objects.Player import Player
from game.World import World
from util import config
import pygame

class Game(object):
    
    def __init__(self):
        self.is_running = False
        
        self.screen = pygame.display.set_mode(config.SCREEN_SIZE, pygame.RESIZABLE)
        
        self.world = World()
        self.player = Player()
        
    
    
    def handle_input(self):
        pass
    
    def update(self, dt):
        self.world.update(dt=dt)
        self.player.update(dt=dt)
    
    def render(self, surface):
        pass
    
    
    
    def run(self, debug=True, profile=True):
        """ 
        Run the game loop
        
        """
        clock = pygame.time.Clock()
        fps = 60
        playtime = 0
        
        self.running = True
        
        if profile:
            import time
            idles, inputs, updates, renders, nidles = [], [], [], [], []
            avg_len = 60

        while self.running:
            if profile:
                t_0 = time.clock()
                
            dt = clock.tick(fps) / 1000.
            playtime += dt
            
            if profile:
                t_idle = time.clock()
                dt_idle = t_idle - t_0
                idles.append(dt_idle)
            
            self.handle_input()
            if profile:
                t_input = time.clock()
                dt_input = t_input - t_idle
                inputs.append(dt_input)
            
            self.update(dt)
            if profile:
                t_update = time.clock()
                dt_update = t_update - t_input
                updates.append(dt_update)
                
            self.render(self.screen)
            if profile:
                t_render = time.clock()
                dt_render = t_render - t_update
                renders.append(dt_render)
                nidles.append(dt_input + dt_update + dt_render)
            
            if debug:
                caption = 'FPS: {: >2.2f}        Playtime: {: >10.2f}s'.format(clock.get_fps(), playtime)
                
            if profile:
                if len(idles) > avg_len:
                    idles.pop(0)
                    nidles.pop(0)
                    inputs.pop(0)
                    updates.pop(0)
                    renders.pop(0)
                
                if debug:
                    caption += '        '
                
                idle_avg = sum(idles) / avg_len
                nidle_avg = sum(nidles) / avg_len
                input_avg = sum(inputs) / avg_len
                update_avg = sum(updates) / avg_len
                render_avg = sum(renders) / avg_len
                caption += 'Idle: {: >3.0f}%        i: {: >5.0f}µs    |    u: {: >5.0f}µs    |    r: {: >5.0f}µs'.format(100 * (idle_avg / (idle_avg + nidle_avg)), 1000000 * input_avg, 1000000 * update_avg, 1000000 * render_avg)
            
            if debug or profile: 
                pygame.display.set_caption(caption)

            pygame.display.flip()
        