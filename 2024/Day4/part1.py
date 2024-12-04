with open('./input.in') as fin:
    data = fin.read().splitlines()


matrix = []
c = 0
word = 'XMAS'

def check_xmas(matrixx):
    ...

# 2D Array aufbauen
# for line in data:
#     line = line.strip()
#     matrix.append(list(line))
    
    
# Nach einem X in der Zeile suchen
for i, liste in enumerate(matrix):
    for j in range(len(liste)):
        if (
            (j < len(liste)-4) and (matrix[i][j] == 'X' and matrix[i][j+1] == 'M' and matrix[i][j+2] == 'A' and matrix[i][j+3] == 'S') or
            (j >= 3) and (matrix[i][j] == 'X' and matrix[i][j-1] == 'M' and matrix[i][j-2] == 'A' and matrix[i][j-3] == 'S') or
            (j >= 3) and (matrix[i][j] == 'X' and matrix[i][j-1] == 'M' and matrix[i][j-2] == 'A' and matrix[i][j-3] == 'S') 
            ):
        

            c += 1
            print(c)
        
   

print(data)
