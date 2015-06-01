'''
Created on May 25, 2015

@author: joep
'''

class Blueprint(object):
    
    def __init__(self, blueprint_id, building_type, floor_plan=None, unlock_condition=None):
        self.blueprint_id = blueprint_id
        self.building_type = building_type
        self._unlock_condition = unlock_condition
        
        self.floor_size = (0, 0)
        self.floor_plan = floor_plan
    
    
    
    @property
    def floor_plan(self):
        return self._floor_plan
    
    @floor_plan.setter
    def floor_plan(self, floor_plan):
        if floor_plan is None:
            self._floor_plan = None
            self.floor_size = (0, 0)
            return
            
        if isinstance(floor_plan, str):
            self._floor_plan = floor_plan.split('\n')
        
        else:
            self._floor_plan = floor_plan
        
        max_len = max(len(row) for row in self._floor_plan)
        self.floor_size = (max_len, len(self._floor_plan))
                    
    
    def is_unlocked_by(self, town):
        if self._unlock_condition is None:
            return True
        
        return self._unlock_condition(town)