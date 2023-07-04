from L8_library import BankAccount

# Object creation
account1 = BankAccount(acc_number=100, balance=100)
account2 = BankAccount(acc_number=200, balance=100)

# Withdraw section

account1.withdraw(amount=40)
account2.withdraw(amount=40)

# Deposite section

account1.deposit(amount=20)
account2.deposit(amount=20)

# Transfer section

account2.transfer(amount=20, acc=account1)

print(f"Balance for Account1 : {account1.get_balance()}")
print(f"Balance for Account2 : {account2.get_balance()}")
