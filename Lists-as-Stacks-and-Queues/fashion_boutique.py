stack_of_clothes = [int(x) for x in input().split()]
capacity = int(input())

racks_count = 0
sum_clothes = 0

while stack_of_clothes:
    current_clothes = stack_of_clothes.pop()
    sum_clothes += current_clothes

    if sum_clothes > capacity:
        sum_clothes -= current_clothes
        stack_of_clothes.append(current_clothes)
        racks_count += 1
        sum_clothes = 0
        continue

    if len(stack_of_clothes) == 0:
        racks_count += 1

print(racks_count)