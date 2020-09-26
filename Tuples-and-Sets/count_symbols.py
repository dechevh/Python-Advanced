text = input()
char_dict = {}

for ch in text:
    if ch not in char_dict:
        char_dict[ch] = 0
    char_dict[ch] += 1

for (key, value) in sorted(char_dict.items()):
    print(f"{key}: {value} time/s")
