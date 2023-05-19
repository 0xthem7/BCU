class BankAccount:
	def __init__(self, acc_number, balance=100):
		'''Account number and balance'''
		self.__balance = balance
		self.__acc_number = acc_number

	def get_account(self):
		return self.__acc_number

	def get_balance(self):
		return self.__balance

	def deposit(self,amount):
		self.__balance += amount

	def withdraw(self,amount):
		self.__balance -= amount

	def transfer(self,amount, acc):
		self.__balance -= amount
		acc.deposit(amount)
