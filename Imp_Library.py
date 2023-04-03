# Randomness in Python
import random
#
print(random.choice(range(100)))
print(random.choice([1, 2, 3, 4, 5, 6]))
print(random.choice("Bhanusai"))
print(random.randrange(1, 100, 2))
print(random.random())
print(random.seed(15))
print(random.random())
L=[1,2,3,4,5,6]
random.shuffle(L)
print(L)

# Math Library
import math

print(math.fabs(-25))
print(abs(-10))
print(math.ceil(25.99))
print(math.ceil(200.18))
print(math.floor(-25.185))
print(math.floor(200.185))
print(math.acos(1))
print(max(-25.185, 26, 28, 66, 45, 100))
print(min(-25.185, 26, 28, 66, 45, 100))


# strings

score = 123
name = "Bhanu sai"
print("hey", name + ",My score is", score)
print("hey %s , my score is %d " % (name, score))

myStr = "Hello world"
print(myStr[2:])
print(myStr[:6] + "India")
print(myStr.swapcase())
user="                                                                         Bhanu  " \
     "" \
     "                 "
print(user.strip())


# list-- append,insert,remove,del,reverse,pop,sort,count,extend

# Tuples and Dictionary --- update,clear,len
mytags=("Name","Lname","Age","Phone")
myone=dict.fromkeys(mytags)
print(myone)
