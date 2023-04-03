number = int(input("enter a number: "))

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print("This is not a prime number:", number)
            print(i, "times", number // i, "is", number)
            break
    else:
        print("The number is prime:", number)

# if 7 is dividable by 2 then it not a prime number if not increase i value and check 
