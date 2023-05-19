# taking input and coverting into integer
a = int(input("Provide side a: "))
b = int(input("Provide side b: "))
c = int(input("Provide side c: "))

# If condition to check weather it is a triangle or not 
def  isTriangle(a,b,c):
	if a < b+c and b < a+c and c < a+b:
		return True
	else:
		return False



if isTriangle(a, b, c):
	perimeter = (a+b+c)/2 # Finding out perimeter 
	area = (perimeter*(perimeter - a)*(perimeter - b)*(perimeter - c))**1/2 #Finding out area
	print('%d is perimeter '%perimeter)
	print('%d is area'%area)
else:
	print("Not a triangle")