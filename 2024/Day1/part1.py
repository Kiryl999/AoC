with open('input.in') as fin:
    data = fin.readlines()

summe = 0
left = []
right = []

for line in data:
    line = line.strip()
    words = line.split()

    left.append(int(words[0]))
    right.append(int(words[1]))
    

left.sort(reverse=False)
right.sort(reverse=False)


diff = [abs(l - r) for l, r in zip(left, right)]

summe = sum(diff)

print("Differenzen:", summe)