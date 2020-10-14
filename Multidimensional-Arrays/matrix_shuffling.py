def input_is_valid(tokens, row, col):
    if tokens[0] != "swap" and len(tokens) != 5:
        return False
    elif int(tokens[1]) and int(tokens[3]) > row:
        return False
    elif int(tokens[2]) and int(tokens[4]) > col:
        return False
    return True


def swap_matrix(matrix, row1, col1, row2, col2):
    value_one = matrix[row1][col1]
    value_two = matrix[row2][col2]
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if i == row1 and j == col1:
                matrix[i][j] = value_two
            elif i == row2 and j == col2:
                matrix[i][j] = value_one
    return matrix


row, col = [int(x) for x in input().split()]
matrix = [[str(y) for y in input().split()] for _ in range(row)]

tokens = input()
current_matrix = matrix

while tokens != "END":
    tokens = tokens.split()
    if input_is_valid(tokens, row, col):
        row1, col1, row2, col2 = int(tokens[1]), int(tokens[2]), int(tokens[3]), int(tokens[4])
        action = swap_matrix(current_matrix, row1, col1, row2, col2)
        print('\n'.join([' '.join(map(str, row)) for row in action]))
    else:
        print(f"Invalid input!")
    tokens = input()
