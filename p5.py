n = input("Enter the number:")
def sum_digits(n):
    sum1=0
    for i in n:
        sum1=sum1+int(i)
    return sum1
print(sum_digits(n))


##wirt function that computes the sum of the digits in an integer . use the following method header:
#for ex ,sum_digits(234) returns 9 (2+3+4)
