print("*******WELCOME TO OUR BANK*******")

user_name=input(("Please enter your name: "))

balance = 1000
op=True

while op : #student completes while loop
    print("\n\n Choose 1 for Deposit \n Choose 2 for Withdraw \n Choose 3 for Check Balance \n Choose Q or q to Exit:")
    choice = input("Please choose transactions:")
    if choice == "1": #user chooses 'deposit'
        funds = int(input("Deposite amount : "))
        balance += funds

    elif choice == "2":
        w_amount = int(input("Withdraw amount : "))
        if w_amount > balance:
            print('It is not possible to withdraw beyond the account balance')
        else:
            balance -= w_amount

    elif choice=="3":
        print("Total balance is %d"%balance)
      
    elif  choice.lower() == "q": #user chooses 'exit'
        
        print("""
    -------------------------------------
   | Thanks for choosing us as your bank |
   | Visit us again!                     |
    -------------------------------------
        """)
        op= False #student does this part too
    else:
        print("Wrong transaction! Try again.")

   