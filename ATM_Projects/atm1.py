print("Good day !")
print("Welcome to Digital Fortress Community Bank")

#card_num = 4212987876565434
password = 1234
balance = 1000
option = 0
#withdraw = 0
Trials = 3

#user_card = input("Please enter your card number: ")
pin = int(input("Please enter your 4 digit PIN: \n"))

if pin == password:
    while option != 4:
        print("********Menu*********")
        print("1: Check Balance")
        print("2: Deposit Amount")
        print("3: Withdraw Amount")
        print("4: Exit Transaction")
        option = int(input("Please choose your option: \n"))
        
        if option == 1:
            print(f"Account Balance is: USD {balance}")
        elif option == 2:
            deposit = int(input("Please Enter your deposit amount: \n"))
            balance += deposit
            print(f" Deposited Amount is: USD {deposit}")
            print(f"Your New balance is: {balance} ")
        elif option == 3:
            withdraw = int(input("Please Enter your withdrawal amount: \n"))
            balance -= withdraw
            print(f" Withdrawal Amount is: USD {withdraw}")
            print(f"Your New balance is: USD {balance}") 
        elif option == 4:
            print("Thank for choosing Digital Frotress, Good bye !")

else:
    print("Incorrect PIN entered, Please Try Again")