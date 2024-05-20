
## Two Dimensional aarays

num_grid = [
[1, 3, 2, 4, 7],
[8, 7, 9, 0, 1],
[0, 2, 3, 1, 2],
[0]
]

print(num_grid[3][0])

for row in num_grid:
    print(row)

for row in num_grid:
    for col in row:
        print(col)
        


num1 = 1234
print(str(num1)[::-1])