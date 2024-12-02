with open('/Users/kiryl/Desktop/FH Studium/AdventofCode/2022/Day3/input.in') as fin:
    data = fin.readlines()
    
summe = 0
scores = {chr(i): i - 96 for i in range(97, 123)} # kleinbuchstaben
scores.update({chr(i): i - 64 + 26 for i in range(65, 91)}) # großbuchstaben


group_list = []
for line in data:
    line = line.strip()
    group_list.append(line)

    if len(group_list) == 3:
        temp = []
        

        for index, char in enumerate(group_list[0]):
            if char in group_list[1] and char in group_list[2] and char not in temp:
                temp.append(char)
                #zeile = zeile[:index] + zeile[index+1:]
                summe += scores[char]
                
        group_list.clear()        
    
print(summe)
                
    