import sys

t = int(input())
for _ in range(t):
    n = int(input())
    phone_numbers = [sys.stdin.readline().rstrip() for _ in range(n)]
    phone_numbers.sort()
    yes = True
    for i in range(len(phone_numbers) - 1):
        p1 = phone_numbers[i]
        p2 = phone_numbers[i + 1]
        if p1 == p2[:len(p1)]:
            yes = False
            break

    if yes:
        print('YES')
    else:
        print('NO')
