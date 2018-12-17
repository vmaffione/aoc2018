f = open("2.first.input", "r")
lines = f.readlines()
f.close()

i = 0
n = len(lines)
while i < n - 1:
    j = i + 1
    while j < n:
        a = lines[i]
        b = lines[j]
        k = 0
        diffk = -1
        l = len(a)
        cdiff = 0
        while k < l:
            if a[k] != b[k]:
                cdiff += 1
                if cdiff > 1:
                    break
                diffk = k
            k += 1
        if cdiff == 1:
            # Pop character at position 'diffk'
            result = a[:diffk] + a[diffk+1:]
            print(result)
        j += 1
    i += 1
