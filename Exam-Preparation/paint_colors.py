strings = input().split()

main_colors = ["red", "yellow", "blue"]
secondary_colors = {
    "orange": ("red", "yellow"),
    "purple": ("red", "blue"),
    "green": ("yellow", "blue")
}

made_colors = []

while strings:
    first_element = strings.pop(0)
    second_element = ""
    if strings:
        second_element = strings.pop()

    first_comb = first_element + second_element
    second_comb = second_element + first_element

    if first_comb in main_colors or first_comb in secondary_colors:
        made_colors.append(first_comb)
    elif second_comb in main_colors or second_comb in secondary_colors:
        made_colors.append(second_comb)
    else:
        if len(first_element) > 1:
            strings.insert(len(strings) // 2, first_element[:-1])
        if len(second_element) > 1:
            strings.insert(len(strings) // 2, second_element[:-1])

for i in range(len(made_colors) - 1, -1, -1):
    current = made_colors[i]
    if current in secondary_colors and any(x not in made_colors for x in secondary_colors[current]):
        del made_colors[i]

print(made_colors)