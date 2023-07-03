s = input()

changed = 0

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        changed += 1

print((changed + 1) // 2)
