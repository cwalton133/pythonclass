## Assignment
 

num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))
num3 = int(input("Enter the number: "))
 
if (num1 > num2 and num1 > num3):
     print("Num1 is the greater Number")
elif (num2 > num31 and num2 > num3):
    print("Num2 is the greater Number")
else:
    print("Num3 is the greater Number")
 
## 1. Write a Python program to check if a given number is even or odd using if and else statements.
num_1 = int(input("Enter number: "))
divider = 2
#num_2 = 3

if num_1 % divider == 0:
    print("Number entered is an Even Number")
else:
    print("Number entered is an Odd Number")

## 2. Create a program that asks the user to input their age and then outputs whether they are eligible to vote or not using if and else.
voting_age = 18
age = int(input("Enter your age: ?"))
voting_age >= age
if age >= voting_age:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
    
    
## 3. Write a Python program that takes a user input for a number and prints "Positive" if it's greater than zero, "Negative" if it's less than zero, and "Zero" if it's equal to zero using if, elif, and else.

num1 = int(input("Enter a number: "))

if num1 > 0:
    print("Positive")
elif num1 < 0:
    print("Negative")
elif num >= 0:
    print("Zero")
else:
    print("Please enter a valid number")
    
    
## 4. Create a program that checks whether a user-inputted number is divisible by both 3 and 5 using if, elif, and else statements. 
number_divisible = int(input("Please anter a valid number: "))

divider1 = 3
divider2 = 5
number_divisible % divider1 and number_divisible % divider2 == 0


if number_divisible % divider1 == 0:
    print("Number is divisible by 3")
elif number_divisible % divider2 == 0:
    print("Number is divisible by 5")
    
else:
    print("The number entered is not divisible by either 3 or 5")

## 5. Write a Python program that compares two numbers provided by the user and prints the larger number using if and else. 
_num1 = int(input("Enter second number: "))
_num2 = int(input("Enter second number: "))

_num1 > _num2 or _num2 > _num1
if _num1 > _num2 == True:
    print(f'{_num1} ">" {_num2}')
elif _num2 > _num1 == True:
    print(f'{_num2} ">" {_num1}')
else:
    print("Enter a valid number")
    

## 6. Create a program that takes a user input for a grade (A, B, C, D, or F) and prints "Pass" if the grade is A, B, or C, and "Fail" otherwise using if and else. 
# 90 to 100 = "Excellent"
# 80 to 89 = "Grade B"
# 70 to 79 = "Grade C"
# 60 to 69 = "Grade D"
# 50 to 59 = "Fail"
# 0 to 49 = "Unknown Results"

user_input = int(input("Enter your grade number: "))

if user_input >= 90 and user_input <= 100:
    print("Excellent Grade")
elif user_input >= 80 and user_input <= 89:
    print("Grade B")
elif user_input >= 70 and user_input <= 79:
    print("Grade C")
elif user_input >= 60 and user_input <= 69:
    print("Grade D")
elif user_input >= 50 and user_input <=59:
    print("Fail")
else:
    print("Unknow Result")


## 7. Write a program that asks the user to input their salary and then calculates their tax based on the following conditions: 
##if salary is less than or equal to 5000, tax is 10%; if salary is between 5001 and 10000, tax is 20%; otherwise, tax is 30% using if, elif, and else. 

salary =int(input("Enter your salary: "))

tax1 = (salary * 10) / 100
tax2 = (salary * 20) / 100
tax3 = (salary * 30) / 100

if salary <= 5000:
    print(f'Your Tax payable is: {tax1}')
elif salary == 5001 or range(0, 10000):
    print(f'Your Tax payable is: {tax2}')
else:
    print(f'Your Tax payable is: {tax3}')


## 8. Create a program that asks the user to input two numbers and then checks if their sum is greater than 100. If it is, print "Sum is greater than 100", otherwise print "Sum is not greater than 100" using if and else. 

## 9. Write a Python program that takes three numbers from the user and prints the largest among them using nested if-else statements. 


## 10. Create a program that takes a user input for their age and then checks if they are eligible for a senior citizen discount (age 60 or above). If they are eligible, print "You are eligible for a senior citizen discount", otherwise print "You are not eligible for a senior citizen discount" using if and else.

user_age = int(input("Enter your age: ?"))

eligible_age = 60
if user_age >= eligible_age:
    print("You are eligible for a senior citizen discount")
else:
    print("You are not eligible for a senior citizen discount")