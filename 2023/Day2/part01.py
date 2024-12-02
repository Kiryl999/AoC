with open("/Users/kiryl/Desktop/FH Studium/AdventofCode/2023/Day2/input.in") as fin:
    data = fin.readlines()
    
summe = 0
colors = ['red', 'blue', 'green']
for i, line in enumerate(data):
    game_id = i + 1
    valid = None
    for k, char in enumerate(line):
        anz = None
        
        for j, color in enumerate(colors):
            if (line[k:k+len(color)] == color):
                anz = int(line[k-3:k-1])
                if(valid == False):
                    break
                
                if (color == 'red' and anz <= 12) or (color == 'blue' and anz <= 14) or (color == 'green' and anz <= 13):
                    valid = True
                    # print(f"{game_id} " + line[k-3:k-1])
                else: 
                    valid = False
                    # print(anz, color)
        
    if valid == True:
        summe += game_id
    
print(summe)
   
        