from collections import deque

string = deque(input())
stack = []

result = "YES"
while string:
    symbol = string.popleft()
    if symbol in '{[(':
        stack.append(symbol)
    else:
        try:
            popped_symbol = stack.pop()
        except:
            result = "NO"
            break
        if (popped_symbol == '{' and symbol == '}') or (popped_symbol == '[' and symbol == ']') or (
                popped_symbol == '(' and symbol == ')'):
            continue
        else:
            result = "NO"
            break

print(result)
