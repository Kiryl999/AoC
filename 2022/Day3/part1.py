with open('/Users/kiryl/Desktop/FH Studium/AdventofCode/2022/Day3/input.in') as fin:
    data = fin.readlines()
    
summe = 0
scores = {chr(i): i - 96 for i in range(97, 123)} # kleinbuchstaben
scores.update({chr(i): i - 64 + 26 for i in range(65, 91)}) # großbuchstaben

groups = 0

for line in data:

    left, right = line[:len(line)//2], line[len(line)//2:]
    print(left)
    print('--')
    print(right)
    temp = []

    for k, l in enumerate(left):
        for i, r in enumerate(right):
            #print(r)
            if l == r and l not in temp:
                temp.append(l)
                summe += scores[l]
                print(l)
                print(right)
                right = right[:i] + right[i+1:]
                print(right)
                
                # break
                
    
print(summe)
                
    