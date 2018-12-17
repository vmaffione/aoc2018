f = open("1.first.input", "r")
lines = f.readlines()
f.close()
fr = 0
seen = set()
while True:
    for line in lines:
        if fr in seen:
            print(fr)
            quit()
        seen.add(fr)
        ch = int(line)
        fr += ch
