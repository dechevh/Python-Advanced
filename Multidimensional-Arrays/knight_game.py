def is_valid(pos, size):
    row = pos[0]
    col = pos[1]
    return 0 <= row < size and 0 <= col < size


def get_killed_knights(row, col, size, board):
    killed_knights = 0
    rows = [-2, -1, 1, 2, 2, 1, -1, -2]
    cols = [1, 2, 2, 1, -1, -2, -2, -1]
    for i in range(8):
        current_pos = [row + rows[i], col + cols[i]]
        if is_valid(current_pos, size) and board[current_pos[0]][current_pos[1]] == "K":
            killed_knights += 1
    return killed_knights


n = int(input())
board = []
total_kills = 0

for _ in range(n):
    board.append([x for x in input()])

while True:
    most_kills = 0
    to_kill = []

    for row in range(n):
        for col in range(n):
            if board[row][col] == "K":
                killed_knights = get_killed_knights(row, col, n, board)
                if killed_knights > most_kills:
                    most_kills = killed_knights
                    to_kill = [row, col]

    if most_kills == 0:
        break

    to_kill_row = to_kill[0]
    to_kill_col = to_kill[1]
    board[to_kill_row][to_kill_col] = "0"
    total_kills += 1

print(total_kills)


#### Some other solution ####

# def check_if_other_K(i, j, board):  # count for each possible moves on 'L' pattern of this K how many K can reach
#     count = 0
#     if (i - 2 >= 0 and j + 1 < board_size and board[i - 2][j + 1] == 'K'):
#         count += 1
#     if (i - 2 >= 0 and j - 1 >= 0 and board[i - 2][j - 1] == 'K'):
#         count += 1
#     if (i - 1 >= 0 and j + 2 < board_size and board[i - 1][j + 2] == 'K'):
#         count += 1
#     if (i - 1 >= 0 and j - 2 >= 0 and board[i - 1][j - 2] == 'K'):
#         count += 1
#     if (i + 2 < board_size and j + 1 < board_size and board[i + 2][j + 1] == 'K'):
#         count += 1
#     if (i + 2 < board_size and j - 1 >= 0 and board[i + 2][j - 1] == 'K'):
#         count += 1
#     if (i + 1 < board_size and j + 2 < board_size and board[i + 1][j + 2] == 'K'):
#         count += 1
#     if (i + 1 < board_size and j - 2 >= 0 and board[i + 1][j - 2] == 'K'):
#         count += 1
#     return count
#
# board_size = int(input())
#
# board = [list(input()) for i in range(board_size)]
#
# removed = 0
# while True:
#
#     K_list = []
#
#     for i in range(board_size):
#         for j in range(board_size):
#             if board[i][j] == 'K':
#                 count = check_if_other_K(i, j, board)
#                 if count > 0:
#                     K_list.append([count, i, j])  # makes a list with count of reachable Ks and its coordinates
#
#     if not K_list: # if list is empty, end of checking loops
#         break
#
#     K_list = sorted(K_list, key= lambda x: -x[0])  # sort the K by the most "dangerous"
#
#     i, j = K_list[0][1], K_list[0][2]  # get the most "dangerous" K coordinates
#     board[i][j] = '0'  # remove this K
#     removed += 1  # increment the number of removed K
#
# print(removed)