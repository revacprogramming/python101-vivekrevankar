class Menu(dict):
  def __str__(self):
    return "\n".join("".join(k,str(v)) for k,v in self.items())

class Order():
  def __init__(self,menu):
   self.menu=menu
   self.orders=dict()
  def __setitem__(self,item,qty):
    self.orders[item]=qty
    
class Bill:
  def __init__(self,item,order):
    self.bill=sum(v*item[k] for k,v in order.orders.items())
  def __str__(self):
    return f"{self.bill} rupees"

m = Menu()
m['pongal']=25
m["idly"] = 20
m["vada"] = 20
m['dosa']=30
m['Tea']=10
m['coffee'] = 10
print('Hi Welcome to Hotel')
choice=input("Do u like to see the Menu y/n:")
if choice =='y':
  print("We have the following Items")
  i=0
  for k,v in m.items():
   i+=1
   print(str(i)+'.'+k,'->',v)
else:
   exit()
print("Accepting your Order and Printing Ur Bill".center(50,'>'))

o = Order(m)
try:
    o["vada"] = 2
    o["pongal"] = 2
except KeyError as e:
    print(e)
b=Bill(m,o)
print(b)