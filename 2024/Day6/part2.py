with open('input.in') as fin:
    matrix = [[j for j in i]for i in fin.read().split('\n')]
# print(matrix)

richtungen = [(-1,0), (0, 1), (1, 0), (0,-1)]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == '^':
            start_x, start_y = j, i
            start_richtung = richtungen[0]   
            break
        
# print(pos_x, pos_y)

c=0

def loop(matrix, x,y,start_richtung):
    pos_x, pos_y, richtung = x,y,start_richtung
    places = set()
    
    while True:
        next_x = pos_x + richtung[1]
        next_y = pos_y + richtung[0]
        
        if 0 <= next_x < len(matrix[0]) and 0 <= next_y < len(matrix):
            if matrix[next_y][next_x] == '#':
                richtung = richtungen[(richtungen.index(richtung) + 1) % 4]
            else:
                pos_x, pos_y = next_x, next_y
                
            if (pos_x, pos_y, richtung) in places:
                return True
            places.add((pos_x, pos_y, richtung))
            
        else:
            break
    

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        tmp = [row[:] for row in matrix]
        tmp[i][j] = '#'
    
        if loop(tmp, start_x,start_y,start_richtung):
            print(c)
            c+=1
  
print(c)