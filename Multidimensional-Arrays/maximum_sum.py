from itertools import chain


def get_squares(matrix):
    squares = []
    for i in range(len(matrix) - 2):
        row = matrix[i]
        for j in range(len(row) - 2):
            square = [
                [matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]],
                [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]],
                [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]]
            ]
            squares.append(square)
    return squares


def get_sum_of_matrix(matrix):
    return sum(chain(*matrix))


def get_max_square(squares):
    max_square = None
    max_square_sum = 0
    for square in squares:
        square_sum = get_sum_of_matrix(square)
        if max_square is None or square_sum > max_square_sum:
            max_square = square
            max_square_sum = square_sum
    return max_square


n, m = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(n)]

squares = get_squares(matrix)
max_square = get_max_square(squares)

print(f"Sum = {get_sum_of_matrix(max_square)}")
print('\n'.join([' '.join(map(str, row)) for row in max_square]))

############## Tanya's solution ##############

# rows, cols = [int(x) for x in input().split()]
# matrix = []
# best_sum = -99999999999999
# best_matrix = []
#
# for _ in range(rows):
#     line = [int(x) for x in input().split()]
#     matrix.append(line)
#
# for row in range(rows - 2):
#     for col in range(cols - 2):
#         sub_matrix = []
#         current_sum = 0
#         row_counter = 0
#         for r in range(row, row + 3):
#             sub_matrix.append([])
#             for c in range(col, col + 3):
#                 sub_matrix[row_counter].append(matrix[r][c])
#                 current_sum += matrix[r][c]
#             row_counter += 1
#         if current_sum > best_sum:
#             best_sum = current_sum
#             best_matrix = sub_matrix
#
# print(f"Sum = {best_sum}")
# for row in best_matrix:
#     print(' '.join([str(x) for x in row]))
