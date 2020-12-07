def get_magic_triangle(n):
    triagnle = [[1], [1, 1]]
    for row in range(2, n):
        new_row = []
        for col in range(0, row + 1):
            if col - 1 < 0:
                new_row.append(1)
            elif col >= len(triagnle[row - 1]):
                new_row.append(1)
            else:
                upper_left = triagnle[row - 1][col - 1]
                upper_right = triagnle[row - 1][col]
                new_value = upper_left + upper_right
                new_row.append(new_value)
        triagnle.append(new_row)
    return triagnle


print(get_magic_triangle(5))
