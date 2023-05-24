"""
list1= [-1,-4,9,8]
new_list=list(filter(lambda x: x>=0, list1))
print(new_list)
"""
def lower_word(i):
    return i.islower()

    
list1=["BUSHRA" , "ALI" , "word" , "number"]
new_list= list(filter(lambda i : i.islower() , list1))
new_list1 =list(filter(lower_word,list1))
print(new_list1)
print(new_list)
                      

