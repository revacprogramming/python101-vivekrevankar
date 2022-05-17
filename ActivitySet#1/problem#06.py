h = float(input("Enter Hours:"))
r = float(input("Enter rate:"))

def computepay(h,r):
    if h>40:
       final_pay=(h*r)+(h-40)*(0.5*r)
    else:
       final_pay=h*r
    return final_pay 

pay= computepay(h,r)
p= pay
print("Pay", p)
