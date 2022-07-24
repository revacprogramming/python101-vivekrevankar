class Menu(dict):
    def __init__(self):
      pass

    def dict(self,item,rate):
      self[item]= rate 


m = Menu()
m["idly"] = 10
m["vada"] = 20

print(m)
for k,v in Menu.itmes():
  print(k,v)

