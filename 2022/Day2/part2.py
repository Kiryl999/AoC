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

loose_scores = {
    'A' : 'Z',
    'B' : 'X',
    'C' : 'Y'
}

scores = {
    'X' :1,
    'Y' :2,
    'Z' :3
}
summe = 0

for line in data:
    line = line.strip().split()
    left.append(line[0])
    right.append(line[1])

for l, r in zip(left, right):
    # score = next(key for key, values in scores.items() if r in values)
    
    if r == 'X':
        o_score = 0
        cum = loose_scores[l]
    elif r == 'Y':
        cum = draw_scores[l]
        o_score = 3
    else: 
        cum = win_scores[l]
        o_score = 6
    score = scores[cum]
    summe += score + o_score
    
print(summe)
    
