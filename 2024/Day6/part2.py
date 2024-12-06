# Eingabedatei einlesen und 2D-Matrix erstellen
with open('input.in') as fin:
    matrix = [[j for j in i]for i in fin.read().split('\n')]
# print(matrix)

richtungen = [(-1,0), (0, 1), (1, 0), (0,-1)] # Mögliche Richtungen 

# Startposition suchen
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == '^':
            start_x, start_y = j, i
            start_richtung = richtungen[0]   
            break
        
# print(pos_x, pos_y)


# Simuliere einen Durchlauf
def loop(matrix, x,y,start_richtung):
    pos_x, pos_y, richtung = x,y,start_richtung # Die Startposition und Richtung
    places = set() # Set am Anfang leeren
    
    # Endlosschleife solang man innerhalb der 2D Matrix ist
    while True:
        # Die nächste Koordinate anhand der Richtung bestimmen
        next_x = pos_x + richtung[1]
        next_y = pos_y + richtung[0]
        
        # Wenn nächste Positon innerhalb der Matrix 
        if 0 <= next_x < len(matrix[0]) and 0 <= next_y < len(matrix):
            
            # Wenn vor den Läufer ein Hinderniss ist
            if matrix[next_y][next_x] == '#':
                richtung = richtungen[(richtungen.index(richtung) + 1) % 4] # 90 Grad Drehung
            else:
                pos_x, pos_y = next_x, next_y # Ein Schritt nach vorne gehen
             
            # Wenn aktuelle Postion und Richtung bereits vorkam, befinden wir uns in einem Loop   
            if (pos_x, pos_y, richtung) in places:
                return True
            
            places.add((pos_x, pos_y, richtung)) # Aktuelle Postion mit Richtung speichern
            
        else:
            break

c=0 # Counter für Anzahl von Loops

# Bruteforce Ansatz: Für jede Koordinate in der Matrix ein Hinderniss hinzufügen
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        tmp = [row[:] for row in matrix]
        tmp[i][j] = '#'

         # Wenn für aktuelle Matrix ein Loop gefunden wird
        if loop(tmp, start_x,start_y,start_richtung):
            print(c)
            c+=1
  
print(c)