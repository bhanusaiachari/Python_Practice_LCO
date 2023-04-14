SuperHero = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(SuperHero)
def getSquare(num):
    return num * num


result = map(getSquare, SuperHero)

result2 = set(result)
print(result2)
