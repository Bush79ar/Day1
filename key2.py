def search (key):
    low=0
    high= len(list1)-1
    while (high >= low):
        mid=(high + low)//2
        if (list1[mid] == key):
            return mid
        elif (list1[mid] > key):
            low= mid+1
        
        else:
            high= mid-1
    
    return -1
list1=[1,2,3,4,5]
print(search(list1,3))

#square root: Given a non-negativ integer 'x' , copute and return the square
#root of 'x' .implement the solution using brnary search
      