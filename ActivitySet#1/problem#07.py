largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else:   
         try:
             n = int(num)
         except:
                 print('Invalid input')
                    
if largest is None:
    largest = n
elif n > largest:
    largest = n
if smallest is None:
    smallest = n
elif n < smallest:
    smallest = n    
    
print("Maximum is", largest)
print("Minimum is", smallest)