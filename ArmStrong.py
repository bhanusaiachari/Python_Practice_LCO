# TODO Custom Code implemented by Bhanu

# Take User input in integer format
num1 = int(input("Enter a number :"))
# Splitting integer into list
num = [int(i) for i in str(num1)]
# print(num)
# initializing sum value to zero
sum = 0
# getting sum value of list
for i in range(0, len(num)):
    sum += num[i]
print("Sum of numbers is : ", sum)

# Cubing the elements in a list num[]
cube_list = [pow(i, len(num)) for i in num]
# printing each element in a list
for i in range(0, len(cube_list)):
    print("Cube of each number :", num[i], "is", cube_list[i])

# Adding all elements in list

cube_sum = 0
for i in range(0, len(cube_list)):
    cube_sum += cube_list[i]
print("Cube sum of all numbers :",cube_sum)
# comparing cube sum with num1

if cube_sum == num1:
    # printing the num is an Armstrong number
    print(num1, "is an Armstrong Number.")
else:
    # printing the num is not an Armstrong number
    print(num1, "is not an Armstrong Number.")
