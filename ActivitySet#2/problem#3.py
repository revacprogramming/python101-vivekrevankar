import re 

def get_cs():
    s = input ("enter the string:");
    return s;

def cs_to_lot(cs):
    list = list(cs.split(';'));
    return list;

def main():
    cs = get_cs()

    lot = cs_to_lot(cs)
    print(lot)


if __name__ == '__main__':
    main() 