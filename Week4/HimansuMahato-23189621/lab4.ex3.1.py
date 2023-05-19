# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 09:29:11 2022

@author: minut
"""

def add(x,y):
    return x + y
def subtract (x,y):
    return x - y
def multipy(x,y):
    return x * y
def divide (x,y):
    return x / y


def calculator(num1,num2,operator):
    if operator == '+':
        print(f'Results: adding {num1} by {num2} = {add(num1,num2)}')
    elif operator == '-':
        print(f'Results: subtracting  {num1} by {num2} = {subtract(num1,num2)}')
    elif operator == '*':
        print(f'Results: multiplying {num1} by {num2} = {multipy(num1,num2)}')
    elif operator == '/':
        print(f'Results: dividing {num1} by {num2} = {divide(num1,num2)}')
    else :
        print('Invaild Input2')

num1 = int(input("input number 1: "))
num2 = int(input("input number 2: "))
operator = input("Select an operator * for multiplication, - for subraction, + for addition, / for division: ")

calculator(num1, num2, operator)
