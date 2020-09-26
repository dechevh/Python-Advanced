n = int(input())

result = set()

for _ in range(n):
    elements = set(input().split())
    result |= elements

print("\n".join(result))
