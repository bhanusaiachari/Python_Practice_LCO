# # if and else ,elif
score = 20
# print("Congrats on High Score:", score)
if score > 30:
    print("hey! Congrats on High Score !!!")
else:
    print("hey! please try again !!!")

print("-------------------Rating System--------------")
rating = int(input("please give your Ratings(1-5): "))
if rating == 5:
    print("Thanks for giving 5 star Rating")
elif rating == 4:
    print("Thanks for giving 4 star Rating")
elif rating == 3:
    print("Thanks for giving 3 star Rating")
else:
    print("We will improve our service !!Thanks for giving valuable feedback ")

# While

a = 0
while (a <= 5):
    print("hola", a)
    a = a + 1
print("your loop ends here")

# for loop
b = list(range(0, 20, 2))
for i in b:
    print(i, end=';')

for i in "Bhanu sai":
    print(i)
# Break and continue pass
L = list(range(0, 20))
U = int(input("enter a value below 20:"))
for i in L:
    if i == U:
        print("we got a match")
        break
else:
    print("No Match")
print("hey im at the for loop outside")

for i in "BhanuSai":
    if i == 'h':
        continue
    print(i)
for i in "BhanuSai":
    if i == 'h':
        pass
    print(i)
