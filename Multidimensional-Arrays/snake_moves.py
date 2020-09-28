from _collections import deque

rows, cols = [int(x) for x in input().split()]
text = deque(input())

matrix = []

for row in range(rows):
    matrix.append([])
    for col in range(cols):
        matrix[row].append("")

for row in range(rows):
    for col in range(cols):
        current_col = col
        current_char = text.popleft()
        if row % 2 != 0:
            current_col = cols - 1 - col
        matrix[row][current_col] = current_char
        text.append(current_char)

for row in matrix:
    print(''.join(row))
