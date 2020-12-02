lines = open("input.txt", "r").read().split("\n")

total1 = 0

for line in lines:
    parts = line.split(" ")
    min, max = [int(part) for part in parts[0].split("-")]
    char = parts[1][0]
    amount = parts[2].count(char)
    if min <= amount <= max :
        total1 += 1

print(total1)


total2 = 0

for line in lines:
    parts = line.split(" ")
    min, max = [int(part) for part in parts[0].split("-")]
    char = parts[1][0]
    if (parts[2][min-1] == char) ^ (parts[2][max-1] == char):
        total2 += 1

print(total2)