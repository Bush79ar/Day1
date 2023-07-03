import numpy as np
l1=[1,2,3,4]
arry1=np.array(l1)
print(arry1)

l2=[11,22,33,44]
arry2=np.array(l2)
print(arry2)

l=[l1,l2] 
print(l)
array_2D=np.array(l)
print(array_2D)
data1=array_2D.shape
print(data1)
data2=array_2D.dtype
print(data2)
data3=np.zeros(3,'int')
print(data3)
data4=np.ones(3)
print(data4)
data5=np.ones([3,3])
print(data5)
data6=np.eye(4)
print(data6)
data7=np.arange(0,50,2)
print(data7)