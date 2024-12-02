with open("/Users/kiryl/Desktop/FH Studium/AdventofCode/2023/Day1/input.txt") as data:
    
    summe = 0
    
    for line in data:
        first = None
        last = None
        
        for i in range(len(line)):
            char = line[i]
            if char.isdigit() and first == None:
                first = int(char)
            
            if char.isdigit():
                last = int(char)
                
        summe += first * 10 + last
    
    print(summe)
    