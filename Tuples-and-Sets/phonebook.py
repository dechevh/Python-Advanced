line = input().split("-")

phonebook = {}

while len(line) != 1:
    name = line[0]
    number = line[1]
    phonebook[name] = number

    line = input().split("-")

n = int(line[0])

for _ in range(n):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
