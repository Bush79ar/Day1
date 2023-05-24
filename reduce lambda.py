from functools import reduce
list1=[1,2,3]
res = reduce(lambda x, y: x + y * y, [list1[:1][0]**2]+list1[1:])
#res = reduce(lambda x, y: x + y ** y,list1)
print(res)