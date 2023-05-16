from random import randint

rand = randint(1,100)
n = False

while not n:
    UrGuess = int(input("Enter Number:"))
    if UrGuess < 1 or UrGuess > 100:
       print("outsid range")
    else:
       if UrGuess == rand:
           print("Is correct")
           n = True
       elif UrGuess > rand:
           print("Go lower")
       else:
            print("Go Hiher")