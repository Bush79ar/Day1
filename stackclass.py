class stacks: 
    def __init__ (self , list1 , st):
        self.list1 = list1
        self.st =st
    
    def list_push(self,list1,st):
        for i in range(len(st)):
            list1.append(st[i])
        return list1
        
    def list_pop(self, list1):
        a = []
        for i in range(len(list1)):
            a.append(list1.pop())
        return a
st = "Hello"
list1=[]
s1= stacks(list1,st)
print(s1.list_push(list1,st))

print(s1.list_pop(list1))


