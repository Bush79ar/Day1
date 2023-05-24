from functools import reduce
list1=[1,2,3]
res = reduce(lambda x, y: x + y **2,list1 ,0)
#res = reduce(lambda x, y: x + y ** y,list1)
print(res)