with open('./input.in') as fin:
    data = fin.read().splitlines()

legit = ['MSSM', 'MMSS', 'SSMM', 'SMMS']          
c = 0

for i, liste in enumerate(data): 
    for j in range(len(liste)):
        if not (0 <= i + 1  < len(data) and 0 <= j+1 < len(liste) and 0 <= i - 1  < len(data) and 0 <= j-1 < len(liste)): continue 
        if data[i][j] == 'A':
            ecken = data[i-1][j-1], data[i-1][j+1], data[i+1][j+1], data [i+1][j-1]
            ecken = list(ecken)
            for legitness in legit:
                legitness = list(legitness)
                
                if ecken == legitness:
                    c += 1
            
print(c)