with open('input.in') as fin:
    data = fin.readlines()
    
left = []
right = []

win_scores = {
    'A' : 'Y',
    'B' : 'Z',
    'C' : 'X'
}

draw_scores = {
    'A' : 'X',
    'B' : 'Y',
    'C' : 'Z'
}

scores = {
    1 :['X'],
    2 :['Y'],
    3 :['Z']
}
summe = 0

for line in data:
    line = line.strip().split()
    left.append(line[0])
    right.append(line[1])

for l, r in zip(left, right):
    score = next(key for key, values in scores.items() if r in values)
    if win_scores[l] == r:
        summe += 6
    elif draw_scores[l] == r:
        summe += 3
    else:
        summe += 0
    
    summe += score
    
print(summe)
