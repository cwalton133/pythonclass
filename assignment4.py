##Assignments
##How work = Assignments


## Basic While Loop 
multiplier = 5
counter = 1
  
while counter <= 10: 
    result = counter * multiplier 
    print(f"{counter} x {multiplier} = {result}") 
    counter += 1
    
    
## User-Defined While Loop 
multiplier = int(input("Enter the multiplier: ")) 
start = 1
end = int(input("Enter the range end: ")) 
  
while start <= end: 
    result = start * multiplier 
    print(f"{start} x {multiplier} = {result}") 
    start += 1


## Nested While Loop (Left-to-Right Format) 
row = 1
  
while row <= 10: 
    col = 1
    while col <= 10: 
        result = row * col 
        print(f"{row} x {col} = {result}", end="\t") 
        col += 1
    print()  # Move to the next line for the next row 
    row += 1
    
    
    product = int(input("Enter a number: \n"))
    for i in range(0, 13):
        print(f'{product} X {i} = {product * 1}')
    