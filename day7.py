sides=int(input("enter the side:"))


def main():
    x = countInputs(sides)
    printCounters(x)
    
def countInputs(sides) :
    counters = [0] * (sides +1)
    for i in counters:
        r = int (input(" Enter the number:"))
        if r <= 6:
             counters[r] = counters [r] +1
    return counters



def printCounters(counters) :
    for i in range(1, len(counters)):
        print(i, " : " , counters[i])

main()

   
    
    


'''

    counters = countInputs(sider)
    printCounters(counters)
'''
    


            
            
        
            
        
    
    
