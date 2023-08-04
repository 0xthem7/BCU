x = [10, 20, 30]
y = x
y.append(40)
print(x)
print(y)
print('-'*10)

x = [[10, 20],[30, 40]]
y = x[:] # y = x.copy()
y[1][0]=100)
print(x)
print(y)
print('-'*10)

# Shallow copy peculiarites
x = [10, 20, 30]
y = x[:]
y.append(40)
print(x)
print(y)

