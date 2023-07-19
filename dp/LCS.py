a = input()
b = input()

arr = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

answer = 0

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            arr[i + 1][j + 1] += arr[i][j] + 1
            answer = max(answer, arr[i + 1][j + 1])
        else:
            arr[i + 1][j + 1] += max(arr[i][j + 1], arr[i + 1][j])

print(answer)

