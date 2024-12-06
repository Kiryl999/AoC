# Eingabedatei einlesen und 2D-Matrix erstellen
with open('input.in') as fin:
    matrix = [[j for j in i]for i in fin.read().split('\n')]
# print(matrix)
places = set()

# Startposition suchen
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == '^':
            pos_x = j 
            pos_y = i  
            places.add((pos_x, pos_y))      
            break
        
# print(pos_x, pos_y)

richtungen = [(-1,0), (0, 1), (1, 0), (0,-1)] # Mögliche Richtungen 
richtung = richtungen[0] # Nach oben laufen ist die Startrichtung

# Endlosschleife solang man innerhalb der 2D Matrix ist
while True:
    # Die nächste Koordinate anhand der Richtung bestimmen
    next_x = pos_x + richtung[1]
    next_y = pos_y + richtung[0]
    
    # Wenn nächste Positon innerhalb der Matrix 
    if (0 <= next_x < len(matrix[0]) and 0 <= next_y < len(matrix)):

        # Wenn vor den Läufer ein Hinderniss ist
        if matrix[next_y][next_x] == '#':
            richtung = richtungen[(richtungen.index(richtung) + 1) % 4] # 90 Grad Drehung
            
        # Gehe ein Schritt entlang der Richtung
        else:
            pos_x, pos_y = next_x, next_y
            places.add((pos_x, pos_y)) # Speichere die aktuelle Postion in einem set
    else:
        break
   
# Lönge des Sets ist die Lösung 
print(len(places))