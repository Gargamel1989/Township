'''
Created on May 17, 2015

@author: joep
'''

class Inventory(object):
    
    class ItemStack(object):
        def __init__(self, item, amount=0):
            self.item = item
            self.amount = amount
    
    def __init__(self):
        self.item_list = []
        self._stacks_of_id = {}
    
    def __len__(self):
        return len(self.item_list)
    
    def __contains__(self, item):
        return item.item_id in self._stacks_of_id
        
    

    
    def ao_item_stacks(self):
        return len(self)
    
    def ao_item(self, item):
        if item not in self:
            return 0
        
        elif item.is_stackable:
            return self.item_list[self._get_stack_index(item)].amount
        
        else:
            return self._stacks_of_id[item.item_id]
    
    def _get_stack_index(self, item):
        for i, stack in enumerate(self.item_list):
            if stack.item.item_id == item.item_id:
                return i
        
        return None
    
    
    
    def add(self, item, amount=1):
        if item.is_stackable:
            if item not in self:
                self._stacks_of_id[item.item_id] = 1
                self.item_list.append(self.ItemStack(item=item))
            
            self.item_list[self._get_stack_index(item)].amount += amount
        
        else:
            if item not in self:
                self._stacks_of_id[item.item_id] = 0
                
            for _ in xrange(amount):
                self.item_list.append(self.ItemStack(item=item, amount=1))
                self._stacks_of_id[item.item_id] += 1
        
    def add_all(self, items):
        for item in items:
            self.add(item)
    
    def remove(self, item, amount=1):
        if item not in self:
            raise InventoryError('Item `{}` is not present in Inventory; can\'t remove'.format(item))
            
        if not item.is_stackable:
            if amount not in [0, 1]:
                raise InventoryError('Cannot remove an amount of an unstackable item')
            removed_item_stack = self.item_list.pop(self._get_stack_index(item))
            self._stacks_of_id[removed_item_stack.item.item_id] -= 1
            if self._stacks_of_id[removed_item_stack.item.item_id] <= 0:
                del self._stacks_of_id[removed_item_stack.item.item_id]
        
        else:
            item_stack_index = self._get_stack_index(item)
            item_stack = self.item_list[item_stack_index]
            if amount > item_stack.amount:
                raise InventoryError('Can\'t remove {} of item {}, only {} are left in the inventory'.format(amount, item, item_stack.amount))
            
            elif amount < 0:
                amount = item_stack.amount
            
            item_stack.amount -= amount
            if item_stack.amount <= 0:
                del self.item_list[item_stack_index]
                del self._stacks_of_id[item.item_id]
            
            
    
    def _remove_one(self, stack_index):
        item_stack = self.item_list.pop(stack_index)
        del self._stacks_of_id[item_stack.item.item_id]
        


class InventoryError(Exception):
    pass