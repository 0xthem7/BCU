# Lab 3 Submission Exercises

n = int(input("Enter a number : "))

root = int(pow(n,0.5)) # Here pow is a function which returns the power of the provided n

check = False

# Divisor check

if n > 2:
	for i in range(2,root+1):
		if n % i == 0:
			check = True
else:
	print('Not a prime number')
	exit()
# Check Evenly divides or not


if check:
	for i in range(1, n):
		for j in range(1,n):
			if i*j == n:
				print(f"{i} * {j} = {n}")
else :
	print("%d is a prime number"%n)

