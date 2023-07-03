N = int(input())

total = N // 5
rest = N % 5

while rest <= N:
    if rest % 3 == 0:
        print(total + (rest // 3))
        exit(0)
    rest += 5
    total -= 1

print(-1)

