from collections import defaultdict

with open ('./input.in') as fin:
    lines = fin.readlines()
    
# Zahl X muss zu einem Zeitpunkt vor Y geprintet werden
# 1. Section definiert Paare was zuerst geprintet wird
pairs = defaultdict(list)
# 2. Was wird geupdatet
updates = []
leerzeichen = False

for line in lines:
    line = line.strip()
    if leerzeichen is True:
        line = line.strip()
        line = line.split(',')
        updates.append(line)
    
    if line != '' and leerzeichen is False:
        left, right = line.split('|')
        pairs[left].append(right)
    else:
        leerzeichen = True
        continue
    
c=0  
summe = 0
valid = True
print(pairs)

for update in updates:
    index_map = {zahl: idx for idx, zahl in enumerate(update)}
    valid = True

    for key, values in pairs.items():
        if key in index_map:
            for value in values:
                if value in index_map:
                    if index_map[key] > index_map[value]:
                        valid = False
                        break
            if not valid:
                break
        
     
    if valid is True:
        # print(index_map)
        length_index = len(update)//2
        summe += int(update[length_index])
                    
           
#print(c)
print(summe)
