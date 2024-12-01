with open('input.in') as fin:
    data = fin.readlines()
    
from collections import defaultdict
    
maxi = 0
current = 0
lel = []
lol = defaultdict(list)
current_key = 1


for i in range(len(data)):
    line = data[i]
    line = line.strip()
    
    print(line)
    
    if line.isdigit():
        number = int(line)
        current += number
        lol[current_key].append(current)
    else:
        current_key += 1
        current = 0
    
    if current > maxi:
        maxi = current
        
   

# max_values = [(key, max(value)) for key, value in lol.items()]
# max_values.sort(key=lambda x: x[1],reverse=True)

max_values = [max(value) for value in lol.values()] # lol.values() gibt alle listen zurück, max(value) gibt max_wert für jeweilige liste zurrück
max_values.sort(reverse=True)

print(max_values[0] + max_values[1] + max_values[2]) 
