#Q2
'''
import math
def area(n,s):
    result= (n*s**2)/4*math.tan(math.pi/n)
    return result
n = int(input("Enter the number of sider:"))
s = float(input("Enter the side:"))
print(area(n,s))

'''
#Q3:
'''
steing= str(input("Enter the name:"))
def countVowels(steing):
    count = 0
    texe =  ['a' ,'e' , 'u' ,'o' , 'i','A'  ,'O' ,'E' ,'O' ,'I']
    for i in steing:
        if i in texe:
            count += 1
    return count
    
print(countVowels(steing))
  '''
#Q1 list

   
#def count(list):
    #count =0
    #list = [22,3,-2,-1,10,1]
    #for i in list:
        #if i < 0 :
          #count += 1
    
    #return count, i print(count(list))
#Q1
'''
list = [22,3,-2,-1,10,1]
count =0
s = 1
for i in list:
    print(i, end=' ')
    if i < 0:
        count=count+1
    s=i*s
print("count:",count)
print("sum",s)
'''
#Q2




 
      
   



 
    
 
 
 
 
 
 
 
