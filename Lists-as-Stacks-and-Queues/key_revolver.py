from collections import deque

price_per_bullet = int(input())
barrel_size = int(input())
bull = list(map(int, input().split()))
bullets = deque(bull[::-1])

locks = deque(list(map(int, input().split())))
intelligence_value = int(input())

total_money = 0

local_barrel = int(barrel_size)
while bullets and locks:

    cur_bullet = bullets.popleft()
    cur_lock = locks.popleft()

    local_barrel -= 1
    total_money -= price_per_bullet

    if cur_bullet <= cur_lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(cur_lock)

    if local_barrel == 0:
        if bullets:
            print("Reloading!")
            local_barrel = int(barrel_size)

if locks and not bullets:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    total_money += intelligence_value
    print(f"{len(bullets)} bullets left. Earned ${total_money}")