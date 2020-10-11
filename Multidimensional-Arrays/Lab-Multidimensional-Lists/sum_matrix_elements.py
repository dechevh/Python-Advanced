import itertools

rows, cols = [int(element) for element in input().split(", ")]
matrix = [[[int(number) for number in input().split(", ")]] for _ in range(rows)]
total = sum(itertools.chain(*matrix))


print(total)
print(matrix)




# rows, cols = [int(element) for element in input().split(", ")]
#
# matrix = []
# total = 0
#
# for _ in range(rows):
#     row = [int(number) for number in input().split(", ")]
#     matrix.append(row)
#     total += sum(row)
#
# print(total)
# print(matrix)
