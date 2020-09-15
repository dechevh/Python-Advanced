from collections import deque

pumps = deque()  # [petrol_yield,kilometers]
tank = 0

n = int(input())  # pumps_count
for _ in range(n):
    pumps.append([int(x) for x in input().split()])

index = 0
while index < n:
    tank = 0
    for i in range(n):
        [amount, distance] = pumps[i]
        tank += amount - distance
        if tank < 0:
            pumps.rotate(-1)
            index += 1
            break  # continue with next pump as start
    else:  # full circle
        break
print(index)