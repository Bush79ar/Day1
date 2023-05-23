"""
def search(key):
    
  
    low=1
    high= key//2
    while (high >= low):
        mid=(high + low)//2
        if (mid*mid == key):
            return mid
        elif (mid*mid < key):
            low= mid+1
        
        else:
            high= mid-1
    
    return -1
key=16
print(search(key))
"""
def search(key):
    
  
    low=1
    high= key//2
    while (high >= low):
        mid=(high + low)//2
        if (mid*mid == key):
            return mid
        elif (mid*mid < key):
            low= mid+1
        
        else:
            high= mid-1
    
    return -1
key=25
print(search(key))