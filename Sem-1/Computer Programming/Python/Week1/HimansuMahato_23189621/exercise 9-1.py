# Roots of a Quadratic Equations
#importing module
from math import sqrt

#Taking input from the user and storing as float variable
A = float(input('Enter the coffecient of A : '))
B = float(input('Enter the coffecient of B : '))
C = float(input('Enter the coffecient of C : '))
# This step uses F staring to print the variables
print('Coffecient of A:',A,'\nCoffecient of B:',B,'\nCoffecient of C:',C)

d = sqrt(B*B-4*A*C)

root1 = (-B+d)/(2*A)
root2 = (-B-d)/(2*A)

print('Root #1 =',root1,'\nRoot #2 =',root2)




# Test 1 
# A = 1, B = 0, C = -4
# Root #1 = 2.0 
# Root #2 = -2.0

# Test 2
# A = 1 , B = 5, C = -36
# Root #1 = 1.1622776601683795 
# Root #2 = -5.16227766016838    

# Test 3
# A = 2, B = 7.5, C = 6
# Root #1 = -1.1569296691827464 
# Root #2 = -2.5930703308172536
                               

# Test 4
# A = 0, B = 3.5, C = 8
# ZeroDivisionError: float division by zero

# Since A is zero; 
# 2*A = 0
# And the we know something divide by zero is undefined that is why ZeroDivisionError is produced
