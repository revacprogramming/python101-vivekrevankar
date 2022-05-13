# Conditional Execution

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
pay = (h * r)
if h>40:
    final_rate=(h-40)*(0.5*r)
    final_pay=pay+final_rate
    print(final_pay)
   
else:
    final_pay=pay
    print(final_pay)
    
    
