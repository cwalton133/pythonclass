#Assigmnes

##1. What is the syntax for creating an empty list in Python? 
##Answer: You can create an empty list in Python using either square brackets [] or the list() function.

## 2. How do you access the third element in a list named my_list? 
my_list = ["ball", "Volleyball", "Basketball"]
#my_list1 = list("ball", "Volleyball", "Basketball")
print(my_list[2])

## 3. Write a Python code snippet to add an element 'apple' to the end of a list named fruits. 

fruits = ['Orange' 'Mango', 'Banana', 'Pineapple']
fruits = fruits.append("Apple")
print(fruits)

##4. How do you remove the third element from a list named numbers? 
print(fruits)

##5. Explain the difference between the append() and extend() methods in Python lists. 
colors = ['Blue', 'Yellow', 'Green']
#fruits.extend(colors)
print(fruits)

##6. Write a Python code snippet to check if an element 'banana' exists in a list named fruits. 


##7. What will be the output of len(['a', 'b', 'c'])? 
alpha = ['a', 'b', 'c']
len(alpha)
print(alpha)

##8. How do you reverse the order of elements in a list named my_list? 
alpha = ['a', 'b', 'c']
a = alpha.reverse()
print(a)

##9. Explain the purpose of the sort() method in Python lists. 

##10. Write a Python code snippet to create a list containing the squares of numbers from 1 to 5.

new_list = ['game', 'running', 'football', 'people', 'Angola']
for item in new_list:
    if 'a' in item:
        print(item)
        
        
## List comprehension examples:
my_list = [item for item in new_list if 'a' in item]
print(my_list)
        
my_list = [item for item in new_list if item != 'football']

my_num = [x for x in range(10)]
my_num = [x for x in range(10) if x <=5]


## Declaring a Tuple 
digital = ('apple', 'banana', 'orange', 'grapefruit')
print(type(digital))
print(digital)
print(len(digital))
print(digital[0])
print(digital[1:2])


##Updating tuple.
digital = ('apple', 'banana', 'orange', 'grapefruit')
mydigital = list(digital)
mydigit[0] = 'Watermelon'
print(tunde)

##Converting it back to Tuple
tunde = tuple(mydigit)
print(tunde)
myclass = tuple(myname)
print(myclass)