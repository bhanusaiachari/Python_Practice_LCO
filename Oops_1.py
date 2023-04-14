class Phone:
    """Simple  class for test"""
    phone_version = "S10"
    brand_name = "Samsung"
    username = ""
    model ="S10+"

    def get_model(self):
        return self.model
    def set_model(self,val):
        self.model ="S10+, " + val





    # Constructor
    def __int__(self, user_name):
        self.username = user_name

    def Bootlogo(self):
        print("SAMSUNG", self.model)


bhanu = Phone()
# bhanu.phone_version="Iphone 14 pro max"
# bhanu.model="S22"
bhanu.set_model("OnePlus")
print(bhanu.get_model())
bhanu.Bootlogo()
