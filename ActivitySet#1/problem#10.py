fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("the file annot be opened", fname)
    quit()
count = 0
total = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confindence:'):
        count = count + 1
        pos = find(':')
        number = line[pos +1:].strip
        num = float(number)
        total = total + num
    
average = total / count
print("Average spam confidence:", average)




