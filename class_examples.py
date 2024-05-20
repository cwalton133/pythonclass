
    ## Declaring how to use classes

class Person():
    name = "Samsung"
    
new_person = Person()
print(new_person.name)


class Person():
    def __init__(self, firstname, lastname, age, origin):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.origin = origin
    def __str__(self):
        return f'{self.firstname}{self.lastname}{self.age}{self.origin}'
    def my_description(self):
        return f'My name is {self.firstname} {self.lastname}I am {self.age} from {self.origin}'
        
new_person = Person("Tunde", "John", 25, "Lagos State")

print(new_person)
print(new_person.my_description())


## Inheriting from a class from another class using the super() function keywords

class MyNew(Person):
    def __init__(self, firstname, lastname, age, origin, serial_number, color):
        super() .__init__ (firstname, lastname, age, origin)
        self.serial_number = serial_number
        self.color = color
    def __str__(self):
        return f'{self.firstname} {self.lastname} {self.age} {self.origin} {self.serial_number} {self.color}'
x = MyNew("Tunde", "Emeka", 38, "Ogun State", 123456, "Color")
print(x)
        

## Set an object for a car, model, color brand and year,

class Car():
    def __init__(self, model, color, brand, year):
        self.model = model
        self.color = color
        self.brand = brand
        self.year = year
    def __str__(self):
        return f"{self.model} {self.color} {self.brand} {self.year}"
new_car = Car("SUV Jeep", "White", "Mecedez", 2012)
print(new_car)


## Looping through a Class object
class Person():
    def __iter__(self):
        self.a = 1
        return self
    def  __next__(self):
        x = self.a
        self.a += 1
        return x
tunde = Person()
tunde1 = iter(tunde)
print(next(tunde1))
print(next(tunde1))
print(next(tunde1))
print(next(tunde1))
print(next(tunde1))
print(next(tunde1))
print(next(tunde1))
print(next(tunde1))
print(next(tunde1))
print(next(tunde1))


## Class Exampls continues

class Car:
    def __init__ (self, brand, model):
        self.brand = brand
        self.model = model
    def tunde(self):
        return f'The name of my car is {self.brand} and the brand is {self.model}'
    
class Phone:
    def __init__(self, brand, name):
        self.name = name
        self.brand = brand
    def tunde(self):
        return f'The name of my phone is {self.name} and the brand is {self.brand}'
    
class School:
        def __init__(self, name, brand):
            self.name = name
            self.brand = brand
        def tunde(self):
            return f'The name of my school is {self.name} and it is recognized as {self.brand}'
        
mycar = Car("toyota", "Camry")
myphone = Phone("Samsung", "Fold")
myschool = School("Unilag School", "Mathematical")

# print(mycar.tunde())
for glory in (mycar, myphone, myschool):
    print(glory.tunde())
    

            
## Sample Class for Hotel Modelling

class Hotel1:
    def __init__ (self, name, description, location, capacity):
                  self.name = name
                  self.description = description
                  self.location = location
                  self.capacity = capacity
    def charles(self):
        return f'The Hotel is {self.name} which is {self.description} which is located at {self.location} it can carry about 400 {self.capacity}'
    

class Hotel2:
    def __init__ (self, name, description, location, capacity):
                  self.name = name
                  self.description = description
                  self.location = location
                  self.capacity = capacity
    def charles(self):
        return f'The Hotel is {self.name} which is {self.description} which is located at {self.location} it can carry about 400 {self.capacity}'

class Hotel3:
    def __init__ (self, name, description, location, capacity):
                  self.name = name
                  self.description = description
                  self.location = location
                  self.capacity = capacity
    def charles(self):
        return f'The Hotel is {self.name} which is {self.description} which is located at {self.location} it can carry about 400 {self.capacity}'

myhotel1 = Hotel1("Desantos Hotel", "Exclusive Hotel", "Akowonjo", "500")
myhotel2 = Hotel2("Eko Meridian Hotel", "Superexclusie Hotel", "Akowonjo", "300")
myhotel3 = Hotel3("Wesley Hotel", "Residential Hotel", "Akowonjo", "1300")

# print(myhotel.tunde())
for hotel in (myhotel1, myhotel2, myhotel3):
    print(hotel.charles())
    
    

x = 20
def myname():
    global x
print(x)
        
myname()


x = 20
def myname():
    tunde = 10
    global x
    def mytunde():
        y = 15
        print(tunde + x + y)
        
myname()


import myimport
myimport.mysum(10, 20)



