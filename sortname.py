array=["said,20", "Majid,19", "salim,32", "ail,21", "sultan,15"]
def insertionsort(array):
    for i in range (1,len(array)):
        key = array[i]
        j =i -1
        #while j >= 0 and key <  array[j]:
        while j >= 0 and key.split(",")[1] <  array[j].split(",")[1]:
            array[j + 1] = array[j]
            j =j-1
            
        array[j+1] = key
        
insertionsort(array)
print(array)
list1=[]
def age_name(array):
    for i in range(len(array)):
        data1=array[i].split(",")
        list1.append(data1[0])
    print(list1)
            

print(age_name(array))


           