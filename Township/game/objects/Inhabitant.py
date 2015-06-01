'''
Created on May 25, 2015

@author: joep
'''

class Inhabitant(object):
    
    def __init__(self, dwelling):
        self.dwelling = dwelling
        self.dwelling.inhabitant = self
        
        self.produced_items = {}
    
    
    
    def produce(self, item_to_produce, amount):
        if not item_to_produce.is_stackable:
            raise AttributeError('Can only produce stackable items, not `{}`'.format(item_to_produce.name))
        if item_to_produce in self.produced_items:
            self.produced_items[item_to_produce] += amount
        
        else:
            self.produced_items[item_to_produce] = amount
    
    