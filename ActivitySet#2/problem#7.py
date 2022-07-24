class Menu():
    def __init__(self,order,rate):
        self.order=order
        self.rate=rate
    
    def __add__(self, other):
      return (self.order+str(self.rate),other.order+str(other.rate) )  

m = Menu("idly", 10)
n=Menu("vada", 20)  

for i in (m+n):
  print(i)