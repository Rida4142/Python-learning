name="Rida"
#this is age 

age=25  #this is age 
"""
This is a multi-line comment
"""

fist_name="Rida"
last_name="Khan"

full_name=fist_name+ " " +last_name 
last_name=full_name* 12

len(fist_name) #this will give the length of the string

len(last_name) #this will give the length of the string
def add(a,b):
    return a+b
add(3,5)

for i in range(11):
    print(i) 
    
for i in range(4,10,2):
    print (i)
    
fruits=["Apple","Banana","Mango"]
print(fruits);

person={
    "name":"Rida",
    "age":21,
    "Degree":"BESE"
}
print(person.items())

def greet(name):
    print("hello")
    
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
factorial(3)

def greet_bob(last_name,first_name="Bob"):
    print("Hello"+" "+first_name+" "+last_name)

greet_bob(first_name="Khan",last_name="alice")