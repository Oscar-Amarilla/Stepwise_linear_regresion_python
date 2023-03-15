#Here are some auxiliary functions; nothing special.

import math

#This is a hat (__--__) function.
def hat(x,init= -math.inf,end=math.inf):
    
    if x >= init and x <= end:
        
        return 1
    
    else:
        
        return 0

#This is a function that set when an element will "appear".
def appear(element, x,init= -math.inf,end=math.inf):
    
    if x >= init and x <= end:
        
        return element
    
    else:
        
        return None
