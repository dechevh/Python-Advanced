from _collections import deque

total_qty = int(input())
orders_queue = deque(map(int, input().split(" ")))
# orders_queue = deque([int(x) for x in input().split(" ")])

print(max(orders_queue))

while orders_queue:
    # take first order
    order = orders_queue.popleft()

    if total_qty >= order:
        total_qty -= order  # remove from total qty
    else:
        # order > total_qty | total_qty < order
        orders_queue.appendleft(order)
        break

if orders_queue:
    orders_left = " ".join(list(map(str, orders_queue)))
    print(f"Orders left {orders_left}")
else:
    print("Orders complete")
