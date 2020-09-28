from _collections import deque

green_light = int(input())
free_window = int(input())
command = input()

cars = deque()
current_seconds = green_light

cars_passed = 0

while command != "END":
    if command != "green":
        cars.append(command)
    else:
        current_seconds = green_light
        ongoing_ch = deque()
        while cars and current_seconds:
            car = cars.popleft()
            for x in car:
                ongoing_ch.append(x)
            while ongoing_ch:
                ongoing_ch.popleft()
                current_seconds -= 1

                if len(ongoing_ch) == 0:
                    cars_passed += 1

        command = input()



    command = input()
