from collections import defaultdict

with open('input.in') as fin:
    data = fin.readlines()

summe = 0  
fallend = None 


for line in data:
    line = line.strip().split()
    valid = True  
    fallend = None  
    problem = None
    print(line)

    for i in range(len(line) - 1):
        diff = abs(int(line[i]) - int(line[i + 1]))  
        
       
        if int(line[i]) < int(line[i + 1]): 
            if fallend is None: 
                fallend = False  
            elif fallend:
                
                valid = False
                break

        elif int(line[i]) > int(line[i + 1]):  
            if fallend is None:  
                fallend = True  
            elif not fallend: 
                valid = False
                break
        
        
        if diff > 3 or diff == 0:
            valid = False
            break
    
    if valid:  
        summe += 1

print(summe)
