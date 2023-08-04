import copy
x = [10, 20, 30]
y = copy.deepcopy(x)
y.append(40)
print(x)
print(y)

