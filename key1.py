'''list1=[1,2,3,4,5]
key =2
s=min(list1)
l1=list1.index(min(list1))
h1=list1.index(max(list1))
mid =(l1+h1)//2

for i in range(len(list1)):
    if (list1[mid] == key):
        print("this key :" , key)
    elif (list1[mid] > key):
        l1=mid+1
        
    elif (list[mid] < key):
        h1=mid-1
    else :
        print(-1)
        '''
def search (list1,key):
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





