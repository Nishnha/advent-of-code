num_valid = 0

with open("input.txt", "r") as input:
    for line in input:
        p = line.split(" ")
        
        count = p[0].split("-")
        min_count = int(count[0])
        max_count = int(count[1])

        letter = p[1].strip(":")
        password = p[2]

        print(min_count, max_count, letter, password)

        occurances = 0
        for c in password:
            if c == letter:
                occurances += 1
        if occurances >= min_count and occurances <= max_count:
            num_valid += 1

print(num_valid)
