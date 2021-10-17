class Product:
    def __init__(self,name,price):
        self.name=name
        self.__price=price
    def showproduct(self):
        print("name:",self.name)
        print("price:",self.__price)
    def calculate(self):
        price=self.__price * (100/50)
        return price
    def set_price(self,price):
        self.__price=price
    def get_price(self):
        return self.__price
prod1=Product('pen',20)
#print(prod1.__price)  __price is private. so it is not accessable form outside class.
prod1.showproduct()
print(prod1.calculate())
print(prod1.get_price())

try:
    fh=int(input('Enter your age :'))
except ValueError:
    print("Enter valid value")#only execute if exception occurs
else:
    print("Success!")#only execute if exception not occur
finally:
    print("finished")#execute  if execption occurs or not
