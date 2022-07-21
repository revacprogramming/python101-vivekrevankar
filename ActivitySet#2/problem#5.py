

def get_cs():
    s = input("enter the string:")


def cs_to_dict(cs):
    d = dict()
    s = cs.split(";")
    for i in s:
      j = i.split("=")
      d[j[0]] = j[1]
      return d

def dict_to_cs(d):
  for i,j in d.items():
    print(i,"=",j,end=";")
     # print(d.keys(),d.values())
    


def main():
    cs = get_cs()

    d = cs_to_dict(cs) # convert connect string to a dictionary
    print(d)

    cs = dict_to_cs(d)
    print(cs)


if __name__ == '__main__':
    main()
