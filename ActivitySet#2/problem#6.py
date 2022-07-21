

class Menu:
    def __init__(self):
      self=dict()

      def add(self,item,price):
        self[item]=price

      def show(self):
        for i,j in self.items():
          print(i,j)



m = Menu()  # Menu is a class
m.add("idly", 10)
m.add("vada". 20)

m.show()
