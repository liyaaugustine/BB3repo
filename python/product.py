class Pmonth:
    def __init__(self,month):
        self.month=month 
    def get_month(self):
        return self.month  
class Product(Pmonth):
    count=0
    def __init__(self,name,category,price,month):
        Pmonth.__init__(self,month)
        self.name=name
        self.category=category
        self.price=price
        Product.count=Product.count+1
    def display_products(self):
        print("name:", self.name)
        print("category:",self.category)
        print("month:" ,Pmonth.get_month(self))
        print("Price:" ,self.price)
    def product_count(self):
        print("Total count of product is: %d" %Product.count)
product1=Product("book","stationary",25,"april")      
product1.display_products()
product1.product_count()
prod2=Product("apple","vegetables",50,"january")
prod2.display_products()
prod2.product_count()




