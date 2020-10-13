from itertools import chain


def get_squares(matrix):
    squares = []
    for i in range(len(matrix) - 1):
        row = matrix[i]
        for j in range(len(row) - 1):
            square = [
                [matrix[i][j], matrix[i][j + 1]],
                [matrix[i + 1][j], matrix[i + 1][j + 1]]
            ]
            squares.append(square)
    return squares


def merge_matrix(matrix):
    return chain(*matrix)


def equal_squares_count(merged_squares):
    count = 0
    for square in squares:
        all_chars = merge_matrix(square)
        if len(set(all_chars)) == 1:
            count += 1
        else:
            pass

    return count


rows, cols = [int(x) for x in input().split(" ")]

matrix = []

for _ in range(rows):
    line = [x for x in input().split()]
    matrix.append(line)

squares = get_squares(matrix)
merged_squares = merge_matrix(squares)
squares_count = equal_squares_count(merged_squares)

print(squares_count)
