def add(a, b):
    c = a+b
    return c


def main():
    a = int(input("enter the first number:"))
    b = int(input("enter the second number:"))

    c = add(a, b)
    print(f"the sum of {a} and {b} is {c}")

main()