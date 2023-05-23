def insertionsort(array):
    for i in range (1,len(array)):
        key = array[i]
        j =i -1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j =j-1
            
        array[j+1] = key
        
array=[6,5,10,7,1]
"""
insertionsort(array)
print(array)
"""


insertionsort(array)
for i in range(len(array)):
    print(array[i] , end=" ")
           