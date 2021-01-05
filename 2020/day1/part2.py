goal = 2020
v = []

with open("input.txt", "r") as input:
    for line in input:
        v.append(int(line.rstrip()))

v = sorted(v)

k = len(v) - 1
for i, x in enumerate(v):
    j = i + 1
    while j < k:
        if v[i] + v[j] + v[k] == goal:
            print(v[i] * v[j] * v[k])
            exit()
        elif v[i] + v[j] + v[k] < goal:
            j = j + 1
        else: # v[i] + v[j] + v[k] > goal
            k = k - 1
