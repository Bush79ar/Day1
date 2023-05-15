string = input("Enter password here:")
l = 0
u = 0
n = 0
s = 0
if len(string) >=8:
    for position in string:
        if position.islower():
            l+= 1
        if position.isupper():
            u+= 1
        if position.isdigit():
            n+= 1
        if (position in '@$#_'):
            s+= 1
            
if (l >= 1 and u >= 1 and n >= 1 and s >= 1 and l+u+n+s == len(string)):
    print("The password is vaild")
else:
    print("The password is  not vaild")
            