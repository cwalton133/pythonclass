
## Udemy Lectures

##. Python 3 - Basics - Defining a variable

my_var = 10 #type integer
my_var = "Hello" #type string
my_var = True #type boolean

##User input
input("Please enter the string you want to be printed out: ")
#Saving the input to a variable
user_says = input("Please enter the string you want to be printed out: ")
#The input of the user is saved as a string by the input() function!

## Python 3 - Strings
#Strings - indexing
a = "Cisco Switch"
a.index("i")
#Strings - character count
a = "Cisco Switch"
a.count("i")
#Strings - finding a character
a = "Cisco Switch"
a.find("sco")
#Strings - converting the case
a = "Cisco Switch"

a.lower() #lowercase
a.upper() #uppercase
#Strings - checking whether the string starts with a character
a = "Cisco Switch"
a.startswith("C")
#Strings - checking whether the string ends with a character
a = "Cisco Switch"
a.endswith("h")
print(a)
#Strings - removing a character from the beginning and the end of a string
a = " Cisco Switch "
a.strip() #remove whitespaces
b = "$$$Cisco Switch$$$"
b.strip("$") #remove a certain character
print(b)
#Strings - removing all occurences of a character from a string
a = " Cisco Switch "
a.replace(" ", "") #replace each space character with the absence of any character
#Strings - splitting a string by specifying a delimiter; the result is a list
a = "Cisco,Juniper,HP,Avaya,Nortel" #the delimiter is a comma
a.split(",")
#Strings - inserting a character in between every two characters of the string / joining the
## Characters by using a delimiter
a = "Cisco Switch"

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
 
print(my_string[-1])

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
 
print(my_string.index("B"))

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
 
print(my_string.count("o"))

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
 
print(my_string.upper())

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
 
print(my_string.find("Bitcoin"))

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
 
print(my_string.swapcase())