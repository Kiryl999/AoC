with open("/Users/kiryl/Desktop/FH Studium/AdventofCode/2023/Day1/input.txt") as data:
    
    summe = 0
    
    nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for line in data:
        first = None
        last = None
        
        for i in range(len(line)):
            char = line[i]
            c = None
            
            for j, num in enumerate(nums):
                if(line[i:i+len(num)] == num):
                    c = j + 1 # Nummber in int konvertieren
                    break
            
            if first == None :
                if (char.isdigit()):
                    first = int(char)
                if (c != None):
                    first = c
                
            
            
            
            if char.isdigit():
                last = int(char)
            if (c != None):
                last = c
                
        summe += first * 10 + last
    
    print(summe)
    