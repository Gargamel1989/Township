'''
Created on May 25, 2015

@author: joep
'''

class Item(object):
    
    def __init__(self, item_id, name, stackable=False):
        self.item_id = item_id
        self.name = name
        self.is_stackable = stackable
    
    def __hash__(self, *args, **kwargs):
        return self.item_id
    
    def __eq__(self, other_item):
        return self.item_id == other_item.item_id