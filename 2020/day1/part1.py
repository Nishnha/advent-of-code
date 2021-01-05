goal = 2020
visited = []

with open("input.txt") as input:
    for j in input:
        i = int(j.rstrip())
        conjugate = goal - i
        if conjugate in visited:
            print(conjugate * i)
        else:
            visited.append(i)

