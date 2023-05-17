'''
n=[[i+1]*3 for i in range(3)]
print(n)
for i in range (3):
    for j in range  (3):
        print(n[i][j] ,end=" ")
       
        
    print()
'''

'''
x=[[1,2,3],
   [4,5,6]]
for i in range(2):
    for j in range(3):
        print(x[i][j],end= ' ')
    print()
'''
#wirting prog where the user determines the number of row and columns , then take
#input from the user for each row and co as 2d list , finally, print the table of the 2d list
'''
x=int(input("Enter the row number:"))
y=int(input("Enter the column number:"))
#b=[[]*y for i in range (x)]
z=[]
for i in range(x):
    a=[]
    for j in range(y):
        n=input("Enter the number:")
        a.append(n)
    z.append(a)

    print(z)  
        #print(z[i][j] , end= '')
for i in range(x):
    for j in range(y):
        print(z[i][j],end=" ")
    print()
'''
'''
 x=[[1,0,0,0],
   [2,1,0,0],
   [2,2,1,0],
   [2,2,2,1]]
   
n=1
z=0
x=2
list2=[]
for i in range (4):
    list1=[]
    for j in range  (4):
        if [i]==[j]:
            list1.append(n)
        if [i]>[j]:
           list1.append(x)
        if [i]<[j]:
            list1.append(z)
    list2.append(list1)
            
for i in range(4):
    for j in range(4):
        print(list2[i][j],end=" ")
    print()
'''
x=0
y=1
list1=[]
for i in range(4):
     a=[]
     for j in range(4):
         z=i+j
         if (z % 2) == 0:
             a.append(y)
         if (z % 2) != 0:
            a.append(x)
     list1.append(a)
for i in range(4):
    for j in range(4):
        print(list1[i][j],end=" ")
    print()
         
            

   









































