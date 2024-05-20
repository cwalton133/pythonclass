
## How to use Functions

def num1(x):
    return x + 10
print(num1(20))

num = lambda a: a + 10
print(num(5))

num = lambda x, y: x * y
print(num(20, 10))

def tunde(h):
    return lambda c: c * h
mytunder = tunde(4)
print(mytunder(10))


def mydouble(x):
    return lambda a: a * x ** 2
mytunde = mydouble(5)
print(mytunde(2))


