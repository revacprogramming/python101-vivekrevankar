dicts = dict()
lst = list()
fname = input('enter the file name:')
try:
    fhand = open(fname)
except:
    print('file cannoted be opened',fname)
    
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
        
    pos = words[5].find(':')
    hour = words[5][:pos]
    if hour not in dicts:
        dicts[hour] = 1
    else:
        dicts[hour] += 1
        
for key, val in list(dicts.items()):
    lst.append((key,val))

lst.sort()
for key, val in lst:
    print(key,val)
