dicts = dict()
fname = input('enter the file:')
try:
    fhand = open(fname)
except:
    print('file cannot be opened:', fname)
    quit()
    
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    if words[1] not in  dicts:
        dicts[words[1]] = 1
    else:
        dicts[words[1]] += 1
        
bigcount = None
bigword = None
for word,count in dicts.items(): 
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print (bigword,bigcount)
