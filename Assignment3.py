#New Assignments

##What is a string in Python? 
##String are phrase or word in double or single quotation mark

##How do you create an empty string? 

my_phrase = ""
print(type(my_phrase))

##Can you access characters in a string using indexing?  Yes
my_phrase1 = "Digital Fortress"
print(my_phrase1[0])

##How do you find the length of a string? 
# myphrase2 = "Hello World"
# print(myphrase2.len())

##How do you concatenate two strings? 
mystring = "Digital Fortress"
welcome = "Here we are"
print(mystring + welcome)
print(f' [mystring] {welcome}')

##How do you convert a string to uppercase? 

phrase = "Hello World"
print(phrase.upper())

##How do you convert a string to lowercase? 
phrase = "Hello World"
print(phrase.lower())

##Can you modify a string once it's created? Yes

##How do you check if a substring exists in a string? 
##we can use the word find function

phrase = "Hello World"
print(phrase.find("World"))
print(phrase.startswith("World"))

##How do you split a string into a list of substrings? 
phrase = "Hello World"
phrase.split()
print(phrase)

##How do you strip whitespace from the beginning and end of a string? 
my_string = "Digital Fortress"
new_string3 = my_string.split(' ').pop()
print(new_string3)

##How do you replace occurrences of a substring within a string?
my_substring = " Digital Fortress "
print(my_substring.strip())


##How do you find the index of a substring within a string? 
my_word = "I Love icecream"
print()

##How do you iterate over the characters of a string? 

##How do you reverse a string in Python? 
n_phrase = "Hello World"
my_phrase4 = n_phrase.split()
my_phrase5 = my_phrase4.reverse()
print(my_phrase5)

##Write a Python expression to check if a string is a palindrome.
def myreverse(s):
    return s == s[:: -1]
print(myreverse('racecar'))
print(myreverse('tundeednut'))

##How do you join elements of a list into a single string? 
my_string = ['Foretress', 'Digital']
new_string = " apple mango".join(my_string)


##How do you convert an integer or float to a string? 
num_1 = input("What is your age: ")
print(type(str(num_1)))


##How do you check if a string contains only digits? 
my_string = "Fortress"
print(my_string.isdigit())

##How do you remove specific characters from a string? 
welcome = "Welcome to Digital Fortress"
welcome.split()
new_welcome  = welcome.pop()
print(new_welcome)



##What is a list in Python? How do you create an empty list? 


##Can you have a list with just one element? 
my_list_2 = ['orange']
print(my_list_2)

## If so, how? How do you access elements in a list? 
fruits_1 = ['orange', 'mango', 'apple', 'lemon']
print(fruits_1[0:3])

##Can you modify the elements of a list after it has been created?

##How do you add an element to the end of a list? 
fruits = ['orange', 'mango', 'apple', 'lemon']
fruits.append('lime')
print(fruits)


##How do you insert an element at a specific position in a list? 
fruits = ['orange', 'mango', 'apple', 'lemon']
fruits.insert(0,'lime')
print(fruits)

##Write a Python expression to find the length of a list. 


##How do you check if an element exists in a list? 

##Write a Python expression to count the occurrences of a particular element in a list.

##How do you remove an element from a list? 
fruits = ['orange', 'mango', 'apple', 'lemon']
fruits.remove('lemon')
print(fruits)

##Can you sort a list in Python? If so, how? 

##How do you reverse a list in Python? 

##Write a Python expression to slice a list.


##How do you iterate over the elements of a list? 
fruits = ['orange', 'mango', 'apple', 'lemon']
for i in fruits:
    print(i[0])
    if i[o] == 'm':
        print(i)
else:
    print('None')

##Write a Python expression to find the maximum element in a list. 

##Write a Python expression to find the minimum element in a list.

##How do you concatenate two lists? 

##How do you convert a list to a string? 

##Write a Python expression to check if two lists are equal.
num1 = 10
num2 = 5
my_num = num1 == num2
print(my_num)

