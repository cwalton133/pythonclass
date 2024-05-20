##Unpacking Turple
##Unpacking Turple

color = ("blue", "yello", "green", "red")
(yam, banana, mango, orange) = color
print(yam) ##it will print out blue

color = ("blue", "yello", "green", "red", "pink", "black")
(yam, banana, *mango) = color
print(mango) ##it will print out ['green', 'red', 'pink', 'black']


for i in color:
    print(i)
    
for i in color:
    print(i[0]) 
    
i = 0 ##initials
while i < len(color):   ## condition
    print(color[i])     ## result
    i +=1               ##increment
    
    
x = 0            ##initials
while x <= 20:   ## condition
    print(x)     ## result
    x +=1        ##increment
    

for i in range(0, 20):
    print(i) 
    

for i in range(0, 20, 2): ## condition and increment by 2
    print(i)
    

for v in range(len(color)):
    print(color[v])
    
## Joining two Turples together
color = ("blue", "yello", "green", "red", "pink", "black")
fruits = ("mango", "yam", "orange", "grape")
print(color + fruits)
print(color * 2)


## Set in dataset
myset = {20, 40, 25, 70, 20, 25, 35}
print(myset)

myset2 = {20, 30, 40, 50, 60}
print(myset2)


myset3 = set((20, 40, 25, 70, 20, 25, 35))
print(myset3)

myset4 = set((20, 40, 25, 70, 20, 25, 35, False, 0, 1, True, 2))
print(type(myset4)) ## It print put the first occurence and left out the last


color2 = set(("blue", "yello", "green", "red", "pink", "black"))
color2.add("cream")
color2.remove("black")
#color2.clear()
print(color2)

for i in color2:
    print(i)


color3 = set(("blue", "yello", "green", "red", "pink", "black"))
fruits3 = set(("yam", "banana", "mango", "orange"))
print(f'{color3} {fruits3}')
myunion = color3.union(fruits3)
print(myunion)


## Dictionary
employee = [
    {
    "name": "Daniel",
    "state": "Lagos State",
    "job" : "Software Development" 
    },
    {
    "name": "Kike",
    "state": "Ogun State",
    "job" : "Software Development"  
        
    },
    {
    "name": "Tade",
    "state": "Rivers State",
    "job" : "Software Develop " 
        
    },
    {
    "name": "Samson",
    "state": "Abia State",
    "job" : "Python Developer"  
        
    }
    
]

print(employee[3]["state"]) ## To access data in a Dictionary

employee[3]["state"]= "FCT" ##To reassign or change a dataset
print(employee[3])

#print(employee['name'])
# print(employee.get("name"))
# print(employee.key())
# print(employee.values())

employee["stae"] = "Ogun State"
employee["email"] = "daniel121@yahoo.com"
employee.update({"name" : "Tunde"})
employee.pop("state")
employee.popitem()
employee.clear()
del employee
print(employee)
