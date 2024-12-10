from collections import defaultdict
from itertools import product

mapp = defaultdict(list)

with open('input.in') as fin:
    data = fin.read().strip().split('\n')

c = 0

# Daten einlesen, und map erstellen
for line in data:
    line = line.strip()
    line = line.split(':')
    line[1] = line[1].strip().split(' ')
    mapp[line[0]] = line[1]
    
    

     
    
    
def elephant(target, values):
    ops = ['+', '*']    
    
    ops_combinations = product(ops, repeat=len(values)-1)
    
    for op_comb in ops_combinations:
        ergebnis = int(values[0])
        
        for i in range(1, len(values)):
            if op_comb[i-1] == '+':
                ergebnis += int(values[i])
            elif op_comb[i-1] == '*':
                ergebnis *= int(values[i])
    
        if ergebnis == int(target):
            return True
        
        
            
 
            
for key in mapp.keys():
    values = mapp[key]
    if elephant(key, values):
        c+= int(key)
        
print(c)