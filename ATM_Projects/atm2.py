print("Welcome to Skye ATM Chammels")
Trials = 3
UserPIn = 1234

while Trials !=0:
    pin = int(input("Enter your PIN number \n"))
    if pin != UserPIn:
        Trials -= 1
        print(f" Wrong PIN Entered, You have {Trials} left")
    else:
        UserChoice = input("D: Deposit or W: Withdrawal or C: Check Balance or E: Exit \n")
        if UserChoice == "D":
            UserDeposit = input("Enter the Amount you would like to Deposit \n")
            print(f"You have deposited {UserDeposit}")
        if UserChoice == "W":
            UserWithdraw = input("Enter the Amount you would like to withdraw \n")
            print(f"You have withdraw {UserWithdraw}")
        UserExit = input("Would you like to continue: Y/N \n")
        if UserExit == "N":
            print("Thank you for using Skye ATM Channel")
            break
        else:
            continue
        
        

            

            
            
    