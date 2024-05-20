
## Python code to demonstrate string length 


## Methods 1: using len
str = "geeks"
print(len(str))


## Method 2: using for loop - Returns length of string
def findLen(str1):
    counter = 0   
    for i in str1:
        counter += 1
    return counter

str1 = "geeks"
print(findLen(str1))


## Method 3: using while loop. --- Returns length of string
def findLen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter

str = "geeks"
print(findLen(str))


## Method 4: using join and count
## Returns length of string
def findLen(str):
    if not str:
        return 0
    else:
        some_random_str = 'py'
        return ((some_random_str).join(str)).count(some_random_str) + 1
 
str = "geeks"
print(findLen(str))


## Method 5: using reduce 

import functools

def findLen(string):
    return functools.reduce(lambda x,y: x+1, string, 0)

# Driver Code
string = 'geeks'
print(findLen(string))


## Method 6: using sum

def findLen(string):
    return sum( 1 for i in string);

# Driver Code
string = 'geeks'
print(findLen(string))


## Method 7: Using enumerate function

## python code to find the length of
## string using enumerate function
string = "gee@1ks"
s = 0
for i, a in enumerate(string):
    s += 1
print(s)







