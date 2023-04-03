# function --- methods
#
def hello():
    print("I want to Learn Python!!!")
    return


hello()

def greetings(str):
    print("Hello", str + " !!!")
    return


greetings("Bhanu")

def user_creation(name,email,phone=0):
    print("Name is :",name)
    print("Name is :",email)
    print("Name is :",phone)

user_creation("Bhanu","Bhanucse.rymec@gmail.com",989898989898989898)

# multiple Arguments

def addle(n1, n2):
    total = n1 + n2
    return total


print(addle(3, 4))

def addle(*num):
    total = 0
    for v in num:
        total = total + v
    return total


print(addle(3, 4, 5, 6, 7, 8))

# Lambda Functions

add = lambda num1, num2: num1 + num2
print(add(3, 4))


