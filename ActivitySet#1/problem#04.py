# Conditional Execution

h = float(input("Enter Hours:"))
r = float(input("Enter rate:"))
pay = (h * r)
if h>40:
    final_pay=(h*r)+(h-40)*(0.5*r)
    print(final_pay)
else:
    final_pay=pay
    print(final_pay)
  