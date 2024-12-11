with open ('input.in') as fin:
    matrix = [[str(j) for j in i]for i in fin.read().split('\n')]
    
richtungen = ((-1,0), (0,1), (1,0), (0,-1))
ans = 0
places = set()

def isHiking(y, x, cur):
    if cur == 9:
        places.add((y,x))
        return 1
    summe = 0
    
    
    for richtung in richtungen:
        dy = y + richtung[0]
        dx = x + richtung[1]
        if 0 <= dy < len(matrix) and 0 <= dx < len(matrix[0]):
            if matrix[dy][dx] == str(cur+1):
                summe += isHiking(dy,dx, cur+1)
                
    return summe
        
        


            

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == '0':
            places.clear()
            lel = isHiking(i, j, 0)
            ans += len(places)
            # print(len(places))
                    
print(ans)
print(places)
                