with open('input.in') as fin:
    matrix = [[j for j in i]for i in fin.read().split('\n')]
# print(matrix)
places = set()

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == '^':
            pos_x = j 
            pos_y = i  
            places.add((pos_x, pos_y))      
            break
        
print(pos_x, pos_y)
richtungen = [(-1,0), (0, 1), (1, 0), (0,-1)]
richtung = richtungen[0]

while True:
    next_x = pos_x + richtung[1]
    next_y = pos_y + richtung[0]
    

    if (0 <= next_x < len(matrix[0]) and 0 <= next_y < len(matrix)):

        if matrix[next_y][next_x] == '#':
            richtung = richtungen[(richtungen.index(richtung) + 1) % 4]
        else:
            pos_x, pos_y = next_x, next_y
            places.add((pos_x, pos_y))
   
    else:
        break
    
print(len(places))