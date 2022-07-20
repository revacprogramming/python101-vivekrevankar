
class test:
    def calculate(self,x,y):
        print(f"The price is {x*y}");

obj = test()
obj.price = 100;
obj.quantity = 5;
obj.calculate(obj.price,obj.quantity);