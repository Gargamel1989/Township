'''
Created on Jun 1, 2015

@author: joep
'''

def are_touching(rect_1, rect_2):
    if rect_1.top == rect_2.bottom or rect_1.bottom == rect_2.top:
        return rect_1.left <= rect_2.left < rect_1.right or \
            rect_2.left <= rect_1.left < rect_2.right
            
    elif rect_1.right == rect_2.left or rect_1.left == rect_2.right:
        return rect_1.top <= rect_2.top < rect_1.bottom or \
            rect_2.top <= rect_1.top < rect_2.bottom
    
    return False