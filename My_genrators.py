import random

heros = ["batman", "hulk", "Thor"]

# for h in heros:
#     print(h)
# g = range(6)
# print(g)

def magic():
    for i in range(6):
        yield random.randint(1,20)
for num in magic():
    print("value is ", num)