with open('input.in') as fin:
    data = fin.readlines()

summe = 0

for left in data:
    left = left.strip()
    left = left.split()
    l = int(left[0])
    counter = 0
    
    
    left.append(int(left[0]))
    for right in data:
        right = right.strip()
        right = right.split()
        r = int(right[1])
        if (l == r):
            counter += 1
        
    temp = l * counter 
    summe += temp
        
    

print("lol:", summe)