start = int(input())
end = int(input())
result = [n for n in range(start, end + 1) if any([n % m == 0 for m in range(2, 11)])]

print(result)
