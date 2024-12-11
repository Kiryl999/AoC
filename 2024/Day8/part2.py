with open('input.in') as fin:
    matrix = [list(line) for line in fin.read().split('\n') if line]
   
   
# print(matrix)
# pos1_found = False 
pos1 = None   
c=0
 
places = set() 
    
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] != '.':
            pos1 = matrix[i][j]
            pos1_coords = (i,j)
            pos1_found = True
            
            for y in range(i, len(matrix)):
                for x in range(len(matrix[0])):
                    if (y, x) != pos1_coords and matrix[y][x] == pos1:
                        pos2_coords = (y,x)
                
                        diff_i = pos2_coords[0] - pos1_coords[0]
                        diff_j = pos2_coords[1] - pos1_coords[1]
                        
                        a1 = (pos1_coords[0] + diff_i, pos1_coords[1] + diff_j)
                        print("---")
                        #print(a1)
                        o=2
                       
                        while(0 <= a1[0] < len(matrix) and 0 <= a1[1] < len(matrix[0])):
                            places.add(a1)
                            # matrix[a1[0]][a1[1]] = "#"
                            diff_i = (pos2_coords[0] - pos1_coords[0])*o
                            diff_j = (pos2_coords[1] - pos1_coords[1])*o
                            a1 = (pos1_coords[0] + diff_i, pos1_coords[1] + diff_j)
                            #print(a1)
                            o+=1
                       
                        
                        diff_i = pos2_coords[0] - pos1_coords[0]
                        diff_j = pos2_coords[1] - pos1_coords[1]
                        a2 = (pos2_coords[0] - diff_i, pos2_coords[1] - diff_j)
                        #print(a2)
                        o=2
                        while(0 <= a2[0] < len(matrix) and 0 <= a2[1] < len(matrix[0])):    
                            places.add(a2)
                            #print(a2)
                            # matrix[a2[0]][a2[1]] = "#"
                            diff_i = (pos2_coords[0] - pos1_coords[0])*o
                            diff_j = (pos2_coords[1] - pos1_coords[1])*o
                            a2 = (pos2_coords[0] - diff_i, pos2_coords[1] - diff_j)
                            o+=1
                            # c+=1
                            
                            
print(len(places))