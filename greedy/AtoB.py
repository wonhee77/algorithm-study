A, B = map(int, input().split())

answer = 0

while True:
    if B < A:
        answer = -1
        break
    if A == B:
        break
    if (B % 10) == 1:
        B = B // 10
    elif (B % 2) == 0:
        B = B // 2
    else:
        answer = -1
        break
    answer += 1

answer = answer + 1 if answer != -1 else -1
print(answer)
