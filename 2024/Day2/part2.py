with open('input.in') as fin:
    data = [line.strip().split() for line in fin.readlines()]

safe_count = 0

for line in data:
    valid = True
    fallend = None

    for i in range(len(line) - 1):
        diff = abs(int(line[i]) - int(line[i + 1]))

        if int(line[i]) < int(line[i + 1]):  # Steigend
            if fallend is None:
                fallend = False
            elif fallend:
                valid = False
                break

        elif int(line[i]) > int(line[i + 1]):  # Fallend
            if fallend is None:
                fallend = True
            elif not fallend:
                valid = False
                break
            
        if diff > 3 or diff == 0:
            valid = False
            break

    if valid:  
        safe_count += 1
        continue

    for j in range(len(line)):
        temp_line = line[:j] + line[j + 1:] 
        valid = True
        fallend = None

        for i in range(len(temp_line) - 1):
            diff = abs(int(temp_line[i]) - int(temp_line[i + 1]))

            if int(temp_line[i]) < int(temp_line[i + 1]): 
                if fallend is None:
                    fallend = False
                elif fallend:
                    valid = False
                    break

            elif int(temp_line[i]) > int(temp_line[i + 1]):  
                if fallend is None:
                    fallend = True
                elif not fallend:
                    valid = False
                    break
                
            if diff > 3 or diff == 0:
                valid = False
                break

        if valid:  
            safe_count += 1
            break

print(safe_count)
