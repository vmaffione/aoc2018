f = open("2.first.input", "r")
lines = f.readlines()
f.close()
count2 = 0
count3 = 0
for line in lines:
    line = line.strip()
    charfreq = dict()
    for c in line:
        if c not in charfreq:
            charfreq[c] = 1
        else:
            charfreq[c] += 1
    freq2 = False
    freq3 = False
    for c in charfreq:
        if charfreq[c] == 2:
            freq2 = True
        if charfreq[c] == 3:
            freq3 = True
    if freq2:
        count2 += 1
    if freq3:
        count3 += 1

print(count2 * count3)
