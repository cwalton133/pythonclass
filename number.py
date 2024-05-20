## Type of Number

#string
# int 
# float
# complex

num1 = "12"
num2 = 12
num3 = 10.00
num4 = 10j

print(type(num1))
print(type(num2))
print(type(num3))
print(type(num4))


num_1 = 10
num_2 = 30
print(num_1 == num_2)
print(num_1 >= num_2)

if num_1 >= num_2:
    print("Num_1 is greater than Num 2")
else:
    print("Num 2 is greater than Num 1")



## Creating of List format
color = ['green', "red", "blue", "pink"]
fruit = ["mango", "banana", "orange", "apple"]
color.extend(fruit)
print(color)
color.pop() # this take out the last number and print out the rest
color.append("Cream") # This would add Cream to the list and print out
color.reverse() # This is used to reverse the number set
print(color.pop()) # This print out he last number
print(color[-1]) # It print out the last number
print(color[2:3]) #this would print from index 2 to the last
print(color[2:]) #sprint from 2 to the last number
print(color[:2]) # Start from the beginning and stop at 2
color.insert(1, "greenyellow")
color.remove("pink")
print(color)


for x in color:
    print(x)
    print(x[1:2])



for i in range(len(color)):
    print(i)