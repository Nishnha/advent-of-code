num_valid = 0

with open("input.txt", "r") as input:
    for line in input:
        valid = False
        x = line.split(" ")
        
        p = x[0].split("-")
        pos1 = int(p[0]) - 1
        pos2 = int(p[1]) - 1

        letter = x[1].strip(":")
        password = x[2]

        print(pos1, pos2, letter, password)

        if password[pos1] == letter:
            valid = not valid
        if password[pos2] == letter:
            valid = not valid

        if valid:
            num_valid += 1

print(num_valid)
