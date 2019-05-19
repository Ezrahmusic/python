# simple calculator 


# this function adds two numbers
def add(num1, num2):
    return num1 + num2


# this function subtracts two numbers
def subtract(num1, num2):
    return num1 - num2


# this function multiplys two numbers
def multiply(num1, num2):
    return num1 * num2


# this function divides two numbers
def divide(num1, num2):
    return num1 / num2


# select inputs
print("""
select input 1,2,3,4
1. add
2. subtract
3. multiply
4. divide
""")

# takes users input
select = input("select operation form 1,2,3,4")

num1 = int(input("enter first number"))
num2 = int(input("enter second number"))

if select == "1":
    print(num1, "+", num2, "=", add(num1, num2))
elif select == "2":
    print(num1, "-", num2, "=",
    subtract(num1, num2))
elif select == "3":
    print(num1, "*", num2, "=",
    multiply(num1, num2))    
elif select == "4":
    print(num1, "/", num2, "/" "=",
    divide(num1, num2))
else:
    print("invalaid input")
