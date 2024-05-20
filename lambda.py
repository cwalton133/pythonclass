
## Declaring lambda functions:

numbers = [20,40, 50, 55, 23, 33, 43, 60]
print(list(filter(lambda x: x % 2 == 0, numbers,)))
print(list(map(lambda u: u % 2, numbers)))