def is_valid(number, size):
    return 0 <= number < size


n = int(input())

bunny_pos = ()
best_sum = -99999999999999999999999999
best_direction = ""

directions = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1),
}
field = []

for row in range(n):
    line = input().split()
    if "B" in line:
        bunny_pos = (row, line.index("B"))
    field.append(line)

for direction in directions:
    current_sum = 0
    row = bunny_pos[0]
    col = bunny_pos[1]

    row_changes = directions[direction][0]
    col_changes = directions[direction][1]

    if not is_valid(row + row_changes, n) or not is_valid(col + col_changes, n):
        continue

    while is_valid(row, n) and is_valid(col, n):
        current_cell = field[row][col]
        if current_cell != "B" and current_cell != "X":
            current_sum += int(current_cell)
        elif current_cell == "X":
            break
        row += row_changes
        col += col_changes

    if current_sum > best_sum:
        best_sum = current_sum
        best_direction = direction

print(best_direction)

row = bunny_pos[0] + directions[best_direction][0]
col = bunny_pos[1] + directions[best_direction][1]

while is_valid(row, n) and is_valid(col, n):
    if field[row][col] == "X":
        break
    print([row, col])
    row += directions[best_direction][0]
    col += directions[best_direction][1]

print(best_sum)
