#Q1:
'''
input_file = open("test.text", "r")
avg_data=0
list1=[]
employee={}
for line in input_file:
    data=line.split()
    #print(data)
    list1.append(float(data[0]))
    employee[data[1]] = data[0]
print(employee)
print(list1)

avg_data = sum(list1)/len(list1)
print( "This avg:",avg_data)
x= max(list1)
for key in employee:
    if(float(employee[key]) == x):

        print("The highest salary:",key ,x)

#input_file.close()
'''
#Q2:
'''
input_file = open("car.txt", "r")
car1=[]
car2=[]
#z= x*y
for line in input_file:
    data=line.split()
    print(data)
    car1.append(int(data[0]))
    car2.append(int(data[1]))
print(car1)
print(car2)
X=car1[0] * car1[0] 
Y=car2[1] * car2[1]
print("The car1:",X)
print("The car2:",Y)

input_file = open("car.txt", "r")
speed = 0
for line in input_file:
    data=line.split()
    print(data)
    speed=int(data[1]) * int(data[0])
    print(speed)
'''
#Q3
input_file = open("m.txt", "r")
n=1
for line in input_file:
    data=line.split()
    print(data)
    if n in range(data):
        n% == 1
    



                
    




