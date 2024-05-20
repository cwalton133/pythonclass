# Python Assignments

words = "Python Programming language is simple" 


## 1. Change the string above to "Python is Easy" and show it in the console.

new_words = words.replace("Python Programming language is simple", "Python is Easy")
print(new_words)

## 2. Find out how many characters are in words above and print it to the console.

words_chars = len(words)
print(words_chars)

## 3. Bring out "Simple" from the above words and show it in the console.
script_part = words[18]
print(script_part)

print(words.split(" ")[4])
print(words[30:37])


## 4. What are the ways to declare variables and the differences between them? 
new_words = "Python is a great programming language" #this is a string
num1 = 23  ##this is an integer number
num2 = 2.6  ##this is an float number
num_1 = 0.922  ##this is an float number
x = 5  ##this is an integer
y = "John" ## x is now of type str
print(type(new_words),(type(num1), type(num2), type(num_1)))


## 5. What are the ways to identify a string? 
# It is always in a words or text
# It must be in double or single quote


## How do I know the position of "s" in simple from the words above? 
print(words.index("s"))
print(words.split(" ")[4][0]) #Better way of doing it


## 7. Create a program that gets 3 numbers from users and multiplies the 3 numbers together and shows the answer in the console
num1 = int(input("Enter your first number: \n"))
num2 = int(input("Enter your second number: \n"))
num3 = int(input("Enter your third number: \n"))
sum_number = num1 * num2 * num3
print(f" The value of the mutiples of is: {num1}  X  {num2}  X {num3}  =  {sum_number}")




## 8. Create a Python code to concatenate two strings "Python" and "Programming".
first_word = "Python"
second_word = "Programming"
print(first_word + " " + second_word)
print(f'(first_word (second_word)')


## 9. Write a Python code to convert the string "HELLO" to lowercase
# phrase = "HELLO"
# print(phrase.lower())


## 10.Create a Python code to extract the substring "World" from the string "Hello, World!".
phrase = "Hello World"
phrase_split = (phrase.split(" "))
print(phrase_split[1])
print(phrase[6:11])

getting_string = phrase.find("world")
i_get = phrase[getting_string : getting_string + len("world")]
print(i_get)



## 11. Write a Python code to check if the substring "Python" exists in the string "I love Python programming"

phrase_1 = "I love Python programming"
print("Python" in phrase_1)
