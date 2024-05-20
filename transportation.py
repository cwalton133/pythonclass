## Write a programm that prints out Bus information

print("Welcome to Favour Transportation !")
print("Please chose your destination")
print('''
1. Egbeda
2. Iyana Ipaja
3. Oshodi
4. Lagos Island
5. Invalid Destination
''')

global egbeda_amount, oshodi_amount, ipaja_amount, lagos_island_amount
egbeda_amount = 300
oshodi_amount = 500
ipaja_amount = 200
lagos_island_amount = 500

def egbeda_dest(passenger_amount):
    if passenger_amount < egbeda_amount:
        print("Not enough money")
    else:
        result = passenger_amount - egbeda_amount
        print(f"\nThank you for choosing Favour Transport\n Your change is {result}\n")

# def oshodi_dest(passenger_amount, oshodi):
def oshodi_dest(passenger_amount):
    if passenger_amount < oshodi_amount:
        print("Not enough money")
    else:
        result = passenger_amount - oshodi_amount
        print(f"\nThank you for choosing Favour Transport\n Your change is {result}\n")  

def ipaja_dest(passenger_amount):
    if passenger_amount < ipaja_amount:
        print("Not enough money")
    else:
        result = passenger_amount - ipaja_amount
        print(f"\nThank you for choosing Favour Transport\n Your change is {result}\n")  


def iplagos_island_dest(passenger_amount):
    if passenger_amount < lagos_island_amount:
        print("Not enough money")
    else:
        result = passenger_amount - lagos_island_amount
        print(f"\nThank you for choosing Favour Transport\n Your change is {result}\n")  



while True:
    destination = int(input("Enter your Destination: \n"))
    if destination > 5:
        print("Invalid destination\n")
        continue
    
    if destination == 1:
        passenger_amount = int(input("Enter amount give to bus conductor: \n"))
        egbeda_dest(passenger_amount)
        break
    elif destination == 2:
        passenger_amount = int(input("Enter amount give to bus conductor: \n"))
        if oshodi_amount < 300:
            print("Not enough money")
        else:
            print(f"Thank you for choosing Favour Transport, your change is {egbeda_dest(passenger_amount, egbeda_amount)}\n")
            break
    elif destination == 3:
        passenger_amount = int(input("Enter amount give to bus conductor: \n"))
        if ipaja_amount < 200:
            print("Not enough money")
        else:
            print(f"Thank you for choosing Favour Transport, your change is {passenger_amount - ipaja_amount}\n")
    elif destination == 4:
        passenger_amount = int(input("Enter amount give to bus conductor: \n"))
        if lagos_island_amount < 500:
            print("Not enough money")
        else:
            print(f"Thank you for choosing Favour Transport, your change is {passenger_amount - lagos_island_amount}\n")
