#
## Condition

# country = "Nigeria"
# age = 20
# if age == 20 and country == "Nigeria":
#      print("You can vote")
# else:
#      print("You can not vote")
     
     
# def greeting():
#     print("Welcome to Digitl Fortress")
# greeting()


# def myclass(x):
#     return x ** 2
# print(myclass(2))

# def myclass(x,y):
#     return x * y
# print(myclass(10,5))


# ##Assignment:
# ## Generate a number that is divisible by 5 should print fixx and if not should print buzz

# num_x = 0
# while num_x <= 21:
#     if num_x % 2 == 0:
#         print("fizz")
# elif num_x % 5 == 0:
#     print("buzz")
# else:
#     print(num_x)
     
     
# myitem = ["Training", "Class", ":item", "tech", "throwback"]
# for i in myitem:
#     #print(i)
#     if i[0] == 't':
#         print(i)
# elif i[0] == 'T':
#     print(i)
    
    
    
## create a programme that checks the greatest number 
## among 3 numbers when a User enter 3 different numbers:

x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))
z = int(input("Enter your third number: "))

if x > y and x > z:
    print(f" {x} > {y} and {z}")
elif y > x and y > z:
    print(f"{y}  > {x} and {z}")
elif z > x and z > y:
    print(f"{z}  > {x} and {y}")
else:
    print("None")