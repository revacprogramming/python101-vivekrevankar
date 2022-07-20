

def get_cs():
  k=input("Enter the sentence:- ")
  return k


def cs_to_lot(cs):
  l=list()
  k=cs.split(";")
  for i in k:
    p=i.split("=")
    n=tuple(p)
    l.append(n)
  return l

def lot_to_cs(lot):
    for i in lot:
      print(i[0],'=',i[1],end=";")


def main():
    cs=get_cs()
    lot=cs_to_lot(cs) 
    print(lot)
    cs=lot_to_cs(lot)  
    print(cs)

if __name__ == '__main__':
    main()