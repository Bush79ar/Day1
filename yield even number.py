nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,15]
def square(nums):
    for num in nums:
         if (num % 2 == 0):
            yield num
v= square(nums)
for i in v:
    print(i)

