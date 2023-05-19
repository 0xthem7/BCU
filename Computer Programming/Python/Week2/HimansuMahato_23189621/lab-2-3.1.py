'''
3.1 Write a program to determine whether a year is leap year based on the given workflow for calculating a leap year.

a) using Nested if 
b) using Elif
c) using Conditional Statement

'''
# Using nested if 
year = int(input("Enter year: "))
if year%4 == 0:
	if year % 100 == 0:
		if year % 400 == 0:
			print('Leap year')
		else:
			print('Not leap year')
	else:
		print('Not leap year')
else:
	print('Not leap year')


# Using Elif 
if year%4 == 0 and year%100 != 0:
	print('Leap year')
elif year%400 == 0 and year%100 == 0:
	print('Leap year')
else:
	print('Not leap year')

# Using conditional
if year%4 == 0 or year%400 == 0 and year%100 != 0:
	print('Leap year')
else:
	print('Not leap year')