number = int(input("enter the number: "))
fact = 1
if number <0:
    print("we dont calculate negative factorials")
elif number ==0:
    print("Result is 1")
else:
    for i in range(1,number + 1):
        fact=fact*i
    print(fact)

# import math
# print(math.factorial(number))