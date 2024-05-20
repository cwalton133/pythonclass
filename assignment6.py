##Assignments

## 1. Write a Python function that takes two numbers as arguments and returns their sum. 

def numbers(x, y):
    return x + y
print(numbers(3,5))

## 2. Create a function that takes a string as input and returns the length of the string. 

# def string_length(phrase):
#     return phrase
# phrase = "Giraffee"
# print.len(("Giraffee"))

# Python code to demonstrate string length 
# using for loop
 
# Returns length of string

def findLen(str):

    counter = 0   

    for i in str:

        counter += 1

    return counter
str = "Digital Fortress"

print(findLen(str)
      
      
# Python code to demonstrate string length 
# using for loop
 
# Returns length of string

string

def findLen(str):

    counter = 0

    while str[counter:]:

        counter += 1

    return counter
str = "Digital Fortress"

print(findLen(str))




## 3. Implement a function that checks if a given number is prime or not and returns True or False accordingly. 

## First Method:

def is_prime(n):
    if n <= 1:
        return True
elif n <= 3:
    return True
elif n % 2 == 0 or n % 3 == 0:
    return False
i = 2
while i * i <= n:
    if n % i == 0 or n % (i % 2) == 0:
        return False
        i +=1
        return True
print(is_prime(7))


## Second Method:

from math import sqrt

def Prime(number,itr):  #prime function to check given number prime or not
  if itr == 1:   #base condition
    return True
  if number % itr == 0:  #if given number divided by itr or not
    return False
  if Prime(number,itr-1) == False:   #Recursive function Call
    return False 
    
  return True
 
num = 13

itr = int(sqrt(num)+1)

## Third Method:

def is_prime(number): 
if number <= 1: 
return False 
for i in range(2, int(number**0.5) + 1): 
if number % i == 0: 
return False
        
              
## 4. Write a Python function that takes a list of numbers as input and returns the sum of all the numbers in the list. 

def list_sum(n):
    total = 0
    for num in n:
        total = total + num
        return total
        mylist = [5,6,7,8,9,10,11,]
        print(list_sum(mylist))


## 5. Develop a function that takes a list of integers as input and returns a new list containing only the even numbers from the original list. 

def even_num(x):
    return [i for i in x if i % 2 == 0]
    numbers = [20, 30, 40, 50, 60]
print(even_num(numbers))  


## 6. Create a function that calculates the factorial of a given number recursively. 

## First Methid:
def factor(n):
    return 1 if (n == 1 or n == 0)
    else (n * factor(n -1))
    num = 4
print(f'{factor(num)}')

## Second Methid:

def factor(n):
    if n == 1:
        return 1
    else:
        return n * factor(n - 1)
 
 ## Third Methid:       
def factor(n):
    if n == 0:
        return 1
    else:
        return n * factor(n - 1)
mynumber = 5
print(myfactor(mynumber))
        
        
## 7. Implement a function that takes a string as input and returns the string reversed. 

def my_string():
    my_name = input("Enter your name:  \n")
    # return my_name.split().reverse()
tunde =  my_name[:: -1]
return tunde
print(my_string)
    
## 8. Write a Python function that checks if a given string is a palindrome (reads the same backward as forward) and returns True or False. 

def my_string1():
    my_name input("Enter your name \n")
    if my_name  == my_name[:: -1]:
        return False
else:
    return True
    
    
## 9. Develop a function that takes a list of strings as input and returns a new list containing only the strings with more than five characters. 

def fruits():
    s = ["apple", "banana", "mango","avocado", "grape", "applemango", "juicyorange"]
for i in s:
    if len(i) > 5:
        print(i)
print(fruits())


## 10. Create a function that takes a list of numbers as input and returns the maximum value in the list.
def my_num2():
    number = [20,30, 40, 50, 60]
    return max(number)
print(my_num2())