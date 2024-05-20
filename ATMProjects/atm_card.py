from CardHolder import cardHolders


def print_menu():    
## print out option menu to the Users
    print("Please choose from one of the following menu: \n")
    print("1: Deposit")
    print("2: Withdrawal")
    print("3: Check Balance")
    print("4: Exit")

def deposit(cardHolders):
    try:
        deposit = float("How much money would you like to deposit \n")
        cardHolders.set_balance(cardHolders.get_balance() + deposit)
        print("Thank you for your $$: Your new balance is ", + str(cardHolders.get_balance()))
    except:
        print("Invalid input, Try again later !")
        
def withdraw(cardHolders):
    try:
        withdraw = float("How much money would you like to withdraw \n")
        ## check if user has enough money in account
        if (cardHolders.get_balance() > withdraw):
            print("Insufficient balance :)")
        cardHolders.set_balance(cardHolders.get_balance() - withdraw)
        print("You are good to go: Thank you  :) ")
    except:
        print("Invalid input, Try again later !")
        
def check_balance(cardHolder):
    print("Your current balance is:", cardHolder.get_balance())
    
if __name__ == "__main__":
    current_user = cardHolders("", "", "", "", "")
    
## create a repo of all card Holders
list_of_cardHolders = []
list_of_cardHolders.append(cardHolders("4532772318790981", 1234, "John", "Smith", 100.34))
list_of_cardHolders.append(cardHolders("4532772318790982", 4545, "Alex", "James", 120.13))
list_of_cardHolders.append(cardHolders("4532772318790983", 6565, "Mathew", "Allen", 7650.15))
list_of_cardHolders.append(cardHolders("4532772318790984", 7712, "Smith", "Michael", 1200.75))


## Prompt Users for Debit card Number
debitCardNum = ""
while True:
    try:
        debitCardNum = input("Please insert your Debit Card \n")
        ## check against repo
        debitMatch = [holder for holder in list_of_cardHolders if holder.cardNum == debitCardNum]
        if (len(debitMatch) > 0):
            current_user = debitMatch[0]
            break
        else:
            print("Card number not recognized, Please try again !")  
    except: 
        print("Card number not recognized, Please try again !")  
        
## Prompt for PIn Number
#userPin = 7712
while True:
    try:
        userPin = int(input("Please enter your 4 digit PIN number: ").strip())
        #userPin = int(input("Please enter your 4 digit PIN number: ").strip()) 
        if (current_user.get_pin() == userPin):
            break
        else:
            print("Invalid PIN, Please try again !")
    except:
        print("Invalid PIN, Please try again !")


## Print out Options

print("Welcome to ABC ATM Chanel", current_user.get_firstname(), " :)")
option = 0
while (option != 4):
    print_menu()
    try:
        option = int(input())
        
    except:
        print("Invalid input, Please try again !")
        
    if option == 1:
        deposit(current_user)
    elif option == 2:
        withdraw(current_user)
    elif option == 3:
        check_balance(current_user)
    elif option == 4:
        break
    else:
        print("Thank you, Have a nice day !")
        