with open('./input.in') as fin:
    data = fin.read().splitlines()

richtungen = [ (0,1), (0,-1), (1,0), (-1,0),
                (1,1), (1,-1), (-1, -1), (-1,1)]
c = 0

for i, liste in enumerate(data):
    for j in range(len(liste)):
        if data[i][j] == 'X': 
            for richtung in richtungen:
                if not (0 <= i + 3 * richtung[0] < len(data) and 0 <= j+3 *richtung[1] < len(liste)): continue 
                if data[i + richtung[0]][j + richtung[1]] == 'M' and data[i+2*richtung[0]][j+2*richtung[1]] == 'A' and data[i+3*richtung[0]][j+3*richtung[1]] == 'S':
                    c+=1
                    print(c)
