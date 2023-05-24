"""c_to_f = lambda x:(x*9/5)+32
print(c_to_f(30))
"""
"""
number = lambda y=5 , x=7 : y*x
print(number(9))
"""
#q1:
#who sort the age:
people = [
{'name':'john', 'age':28},
{'name':'mary', 'age':23},
{'name':'Bob', 'age':35},
{'name':'Alice', 'age':32}
]

print(sorted(people, key=lambda i: i['age']))

people.sort(key=lambda i: i['age'])
print(people)
 



