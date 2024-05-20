# phrase = "Giraffe Academy"
# print(phrase.find("Academy"))

# my_num = 4
# print(my_num)

# num_1 = input("Enter a number: ")
# num_2 = input("Enter another number: ")
# result = float(num_1) + float(num_2)
# print(result)


# num1 = int(input("Enter your first number: \n"))
# num2 = int(input("Enter your second number: \n"))
# num3 = int(input("Enter your third number: \n"))
# sum_number = num1 * num2 * num3
# # print(f'' "The value of the mutiples of " + (num1) + X + (num2) + X (num3)  =  (sum_number)")
# print(f" The value of the mutiples of is: {num1}  X  {num2}  X {num3}  =  {sum_number}")



# name = input('Enter your Name: ')
# age = int(input('Enter your Age: '))
# print(f" Hello {name} you are {age} years old")

# x = 7
# y = 8
# z = 0

# result1 = x == y
# result2 = y > x
# result3 = z < x + 2
# result4 = result1 or result2

# print(result4)


## Forloop Syntax
# for x in range (2, 10):  ## start, stop 
#     print(x)
    
# for y in range (2, 10, 2):  ## start, stop step
#     print(y)
    
# for z in range (0, 10):  ## start, stop step
#     print(z)
    
# for i in range (-10, -1, -1):  ## start, stop step
#     print(i)
    
# for i in range [2, 10,4, 3, 2]:  ## start, stop step
#     print(i)
    
# x = [2,3,4,5,6]
# for i in range (len(x)):  ## start, stop step
#     print(x[i])
    
# x = [2,3,4,5,6]
# for i, element in enumerate (x):  ## start, stop step
#     print(i, element)
    
    
# ## While Loops syntax
# while Condition == True:
#     print(condition)
    
    
# i = 0
# while i < 10:
#     print('run')
#     i += 1
    

## Comprehension
print("Hello" != "Hello")
print("Hello" == "Hello")

countries = ["USA", "UK", "Singapore", "India", "Africa"]
print(countries)
countries.append("Australia")
print(countries)
countries.sort()
print(countries)
countries.reverse()
print(countries)



letters = ["A", "B", "C", "D", "E", "F"]
print(letters[0:2])

students = [
    ["A", "B", "C", "D", "E", "F"]
    #["G", "H", "I", "J", "K", "L"]
    #["M", "N", "O", "P", "Q", "R"]    
]

print(students)

def multiply_values(list):
    multiplied_values = []
    for item in list:
        multiplied_values.append(item * 2)
        return multiplied_values
    print(multiply_values([1,2,3]))
    
    multiply_values()

phrase = "Giraffe Academy"    
print(phrase.lower())

character_age = 25
character_name = "John"

print(f" He like the name {character_name}, but does not like the age {character_age}" )


country_names = ["Brazil", "Argentina", "Spain", "France"]
s.join(country_names)
