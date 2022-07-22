

class Menu:
    def __init__(self,item,rate):
      self.item = item
      self.rate = rate

    def __add__(self,other):
      return(self.item + str(self.rate),other.item + str(other.item))
      

m = Menu()
m = m + ("idly", 10) + ("vada", 20)  # Hint: operator overloading special methods (__add__, __sub__, etc.)

print(m)  # should print the menu properly
