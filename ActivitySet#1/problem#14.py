import re

count = 0                              

input_exp = input('Enter a regular expression: ')
reg_exp = str(input_exp)              
fname = 'mbox.txt'
fhand = open(fname)

for line in fhand:
    line = line.rstrip()

    if re.findall(reg_exp, line) != []:
        count += 1

print(fname + ' had ' + str(count) + ' lines that matched ' + reg_exp)
