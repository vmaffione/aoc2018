import re

f = open("3.first.input", "r")
lines = f.readlines()
f.close()

n = 1024
# Build an nxn array (matrix) with all the elements set to 0
matrix = [0] * (n * n)

for line in lines:
    match = re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)
    claim_id = int(match.group(1))
    left = int(match.group(2))
    top = int(match.group(3))
    width = int(match.group(4))
    height = int(match.group(5))

    for i in range(left, left + width):
        for j in range(top, top + height):
            matrix[i * n + j] += 1

count = sum([1 for c in matrix if c >= 2])
print(count)
