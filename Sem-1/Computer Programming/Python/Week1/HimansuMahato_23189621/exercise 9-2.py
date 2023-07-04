from math import sqrt

# Making varaiable 

a = 9
b = 8
c = 12
d = 33
e = 5
datas = [a,b,c,d,e] # Making a list so that other operation will be easy later on 
summation = 0 # summation to store the summation data
squaredData = [] # stores all the squared data 



mean = (a+b+c+d+e)/5 # x = sum of all numbers / n ; where n is number of data 

# Running for loop to store the square data that is deduced form the mean

for data in datas:
	squaredData.append((data - mean)**2)

# Another for loop to find out the summation of all the squared data 
for data in squaredData:
	summation += data

# Dividing by 5 which gives us the standard deviation
print(sqrt(summation / 5)) # sqrt is a function which gives the square root 

#Output
10.051865498503252
