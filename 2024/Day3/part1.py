with open('./input.in') as fin:
    data = fin.read()
    
summe = 0
i= 0

while i < len(data):
    #print(data[i:i+4])
    if data[i:i+4] == 'mul(':
        i += 4
        inhalt = ''
        
        while data[i] != ')':
            inhalt += data[i]
            if data[i:i+4] == 'mul(': # wenn zwischen durch nach einem neuen mul( gefunden wird
                break
            i += 1
        
        teile = inhalt.split(',')
        # print(teile)
        if len(teile) == 2 and teile[0].isdigit() and teile[1].isdigit():
            print(teile)
            temp = int(teile[0]) * int(teile[1])
            summe += temp
    else:
        i += 1
    
    #print(line)
print(summe)
