# standard type of variables  Numbers,Tuples,strings,list,Dictionary

# Nums and Strings
# int , float, Complex-- x+jy

bank_uid = 1234567
bank_balance = 4566789.0
# del bank_balance
print(type(bank_uid))
print(type(bank_balance))
print('---------String examples-------------')
# strings
str1 = "Hello Bhanu!!!"
print(str1)
print(str1[1])
print(str1[3:5])
print(str1[-1])
print(str1 + "SAI")  # concatenate two strings

# LISTS --- changeable
print('---------Lists examples-------------')
MyList = [1, 2, 3, 4, 5, "Bhanu", 4.6, 5.9]
print(MyList[1])
print(MyList[1:6])
MyList.append(400)
print(MyList)
MyList.remove(5.9)
print(MyList)
MyList.pop(5)
print(MyList)
print(MyList * 2)  # duplicates List
MyList.index(2)
print(MyList)

# Tuples --- not changeable --()
print('---------Tuples examples-------------')
MyTuple = (1, 2, 3, "Bhanu", 5.6, "Sai")
MyTuple2 = (5, 6, 7, 'Ram')
print(MyTuple)
print(MyTuple2)
print(MyTuple[2])
print(MyTuple2[1:3])
print(MyTuple + MyTuple2)
# print(sort(MyTuple))
# print(MyTuple)
# TODO: NOT Valid
# MyTuple[1]="Hello"
# print(MyTuple)


# Dictionary --{key,value}
print('---------Dictionary examples-------------')
Dic = {
    "Name": 'bhanu',
    "Age": 24,
    "role": 'SDE',
    3: [2, 2, 3, 4, 5],
    4: {1, 2, 3, 4, 5, 6, 7, 8, 9}
}
print(Dic)
print(Dic["Name"])
print(Dic.keys())
print(Dic.values())
print(Dic.get(4))
