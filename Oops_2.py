class Samsung:
    def __init__(self):
        print("I'm Samsung")
    def makeScreen(self):
        print("I make Screens")

    def test(self):
        print("Screen Test: Ok")
        print("Screen Test 2: Ok")
        print("Screen Test 3: Ok")

class Iphone(Samsung):
    def __init__(self):
        # super().__init__()
        print("im a Iphone")
    def a3chips(self):
        print("I make A3 bionic chips")
    def itest(self):
        print("iphone test : ok")
        super().test()


user = Iphone()
user.a3chips()
user.makeScreen()
user.itest()

