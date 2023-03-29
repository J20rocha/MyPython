import math

def adding(a,b):
    answer= float(a) + float(b)
    
    print(str(a) + "+" + str(b) + "=" + str(answer))
    return a,b, answer

def subtract(a,b):
    answer= float(a) - float(b)
    
    print(str(a) + "-" + str(b) + "=" + str(answer))
    return a,b, answer


def multiply(a,b):
    answer= float(a) * float(b)
    
    print(str(a) + "*" + str(b) + "=" + str(answer))
    return a,b, answer



def divide(a,b):
    answer= float(a) / float(b)
    
    print(str(a) + "/" + str(b) + "=" + str(answer))
    return a,b, answer


#The code will find the specific arithmetic operator

print("Welcome!")
print("This is a basic calculator")

print("Please enter your operation: ")
a=input("A: ")
operator=input("Operator: ")
b= input("B: ")


if "+" in operator:
    adding(a,b)

if "-" in operator:
    subtract(a,b)

if "*" in operator:
    multiply(a,b)

if "/" in operator:
    divide(a,b)